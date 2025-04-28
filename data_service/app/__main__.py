import granian
from granian.constants import Interfaces
from granian.constants import Loops

from .settings import settings

if __name__ == "__main__":
    granian.Granian(  # type: ignore[attr-defined]
        target="app.app:application",
        address="0.0.0.0",  # noqa: S104
        port=settings.app_port,
        interface=Interfaces.ASGI,
        log_dictconfig={"root": {"level": "INFO"}} if not settings.debug else {},
        log_level=settings.log_level,
        loop=Loops.uvloop,
    ).serve()
