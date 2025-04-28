from uuid import UUID

from litestar.contrib.sqlalchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .models import OfferWall
from .models import OfferWallOffer
from .models import OfferWallPopupOffer


class OfferWallRepository(SQLAlchemyAsyncRepository[OfferWall]):

    model_type = OfferWall

    async def get_by_url(self, url: str) -> OfferWall | None:
        return await self.get_one_or_none(
            OfferWall.url == url,
            load=[
                selectinload(OfferWall.offer_assignments).selectinload(
                    OfferWallOffer.offer
                ),
                selectinload(OfferWall.popup_assignments).selectinload(
                    OfferWallPopupOffer.offer
                ),
            ],
        )

    async def get_with_assignments(self, token: UUID) -> OfferWall | None:
        return await self.get_one_or_none(
            OfferWall.token == token,
            load=[
                selectinload(OfferWall.offer_assignments).selectinload(
                    OfferWallOffer.offer
                ),
                selectinload(OfferWall.popup_assignments).selectinload(
                    OfferWallPopupOffer.offer
                ),
            ],
        )


async def provide_offerwall_repo(db_session: AsyncSession) -> OfferWallRepository:
    return OfferWallRepository(session=db_session)
