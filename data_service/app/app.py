import litestar
from litestar.openapi import OpenAPIConfig

from .api.offer_walls import route as offer_walls_route
from .database import sqlalchemy_plugin
from .exceptions import handle_not_found
from .exceptions import NotFound
from .settings import settings


def build_app() -> litestar.Litestar:
    print(settings)
    print(settings.db_dsn)
    return litestar.Litestar(
        debug=settings.debug,
        plugins=[sqlalchemy_plugin(settings)],
        route_handlers=[offer_walls_route],
        exception_handlers={NotFound: handle_not_found},
        openapi_config=OpenAPIConfig(
            title="Litestar offerAdmin API",
            version="0.0.1",
        ),
    )


application = build_app()
