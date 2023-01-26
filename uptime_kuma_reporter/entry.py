from mcdreforged.api.types import PluginServerInterface as PSI
from mcdreforged.api.decorator import new_thread
from .config import Config
import schedule
import urllib.request as req
from urllib.parse import urlencode
import warnings


job: schedule.Job
config: Config

def report(msg="OK"):
    status = "up" if PSI.get_instance().is_server_running() else "down"
    _report(status, msg=msg)

def _report(status: str, msg: str = "OK", ping: int = 0):
    if config.url == "":
        warnings.warn("Report url is not setup!")
        return
    data = { "status": status, "msg": msg, "ping": ping }

    url = config.url + '?' + urlencode(data)
    if config.log_push:
        PSI.get_instance().logger.info(f"reporting: {url}")
    try:
        request = req.Request(url, headers= {'User-Agent' : "MCDR Reporter"})
        req.urlopen(request)
    except Exception:
        pass

@new_thread("UptimeKumaReporter")
def start_job():
    global job
    job = schedule.every(config.interval).seconds.do(report)
    while True:
        schedule.run_pending()

def on_load(server: PSI, prev_module):
    global job, config
    server.logger.info("UptimeKuma Reporter enabled.")
    config = server.load_config_simple(target_class=Config)
    report("Plugin loaded")
    start_job()

def on_unload(server: PSI):
    global job
    schedule.cancel_job(job)
    _report("down", "UptimeKumaReporter plugin unload")

def on_server_startup(server: PSI):
    _report("up", "Server started.")

def on_server_stop(server: PSI, code: int):
    msg = "Server stopped." if code == 0 else f"Server crash with code {code}"
    _report("down", msg)
    
