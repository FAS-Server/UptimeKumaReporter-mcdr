from mcdreforged.api.utils import Serializable

class Config(Serializable):
    url: str = ""
    interval: int = 60
    log_push: bool = False
