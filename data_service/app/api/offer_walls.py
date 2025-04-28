from uuid import UUID

from litestar import Controller
from litestar import get
from litestar import Router
from litestar.di import Provide
from litestar.openapi import ResponseSpec
from litestar.openapi.spec import Example

from app.exceptions import NotFound
from app.models import OfferChoices
from app.models import OfferWall
from app.repository import OfferWallRepository
from app.repository import provide_offerwall_repo
from .dto.offerwalls_model_dto import ReadOfferWallDTO


class OfferWallContoller(Controller):
    path = ""
    dependencies = {"offer_walls_repo": Provide(provide_offerwall_repo)}

    @get("/{token: uuid}", return_dto=ReadOfferWallDTO)
    async def get_offerwall(
        self, token: UUID, offer_walls_repo: OfferWallRepository
    ) -> OfferWall:
        offerwall = await offer_walls_repo.get_with_assignments(token)

        if offerwall is None:
            raise NotFound

        return offerwall

    @get("/by_url/{url: path}", return_dto=ReadOfferWallDTO)
    async def by_url(
        self, url: str, offer_walls_repo: OfferWallRepository
    ) -> OfferWall:
        url = url.lstrip("/")
        offerwall = await offer_walls_repo.get_by_url(url=url)

        if offerwall is None:
            raise NotFound

        return offerwall

    @get(
        "/get_offer_names",
        responses={
            200: ResponseSpec(
                data_container=dict,
                examples=[Example("response", value={"offer_names": ["Loanplus"]})],
            )
        },
    )
    async def get_offer_names(self) -> dict[str, list[str]]:
        return {"offer_names": list(OfferChoices.__members__.keys())}


route = Router(
    path="/offerwalls",
    route_handlers=[OfferWallContoller],
)
