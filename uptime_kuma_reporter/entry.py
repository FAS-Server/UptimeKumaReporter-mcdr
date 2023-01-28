import time
from mcdreforged.api.types import PluginServerInterface as PSI
from .config import Config
import urllib.request as req
from threading import Event, Thread
from urllib.parse import urlencode
import warnings
import traceback
import functools


config: Config
_psi: PSI

def psi():
    if not _psi:
        _psi = PSI.get_instance()
    return _psi
    

class Reporter(Thread):
    def __init__(self, interval: int):
        super().__init__()
        self.setDaemon(True)
        self.setName(self.__class__.__name__)
        self._report_time = time.time()
        self.stop_event = Event()
        self.interval = interval

    def run(self):
        while True: # loop until stop
            while True: # # loop for report
                if self.stop_event.wait(1):
                    return
                if time.time() - self._report_time > self.interval:
                    break
            self._report_time = time.time()
            report()

    def stop(self):
        self.stop_event.set()

reporter: Reporter

def catch_exceptions():
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                psi().logger.warn(traceback.format_exc())
        return wrapper
    return catch_exceptions_decorator

def report(msg="OK"):
    status = "up" if psi().is_server_running() else "down"
    _report(status, msg=msg)

@catch_exceptions()
def _report(status: str, msg: str = "OK", ping: int = 0):
    if config.url == "":
        warnings.warn("Report url is not setup!")
        return
    data = { "status": status, "msg": msg, "ping": ping }

    url = config.url + '?' + urlencode(data)
    if config.log_push:
        psi().logger.info(f"reporting: {url}")
    request = req.Request(url, headers= {'User-Agent' : "MCDR Reporter"})
    req.urlopen(request)

def on_load(server: PSI, prev_module):
    global config, reporter
    server.logger.info("UptimeKuma Reporter enabled.")
    config = server.load_config_simple(target_class=Config)
    report("Plugin loaded")
    reporter = Reporter(config.interval)
    reporter.start()

def on_unload(server: PSI):
    _report("down", "UptimeKumaReporter plugin unload")
    if reporter:
        reporter.stop()

def on_server_startup(server: PSI):
    _report("up", "Server started.")

def on_server_stop(server: PSI, code: int):
    msg = "Server stopped." if code == 0 else f"Server crash with code {code}"
    _report("down", msg)
    
