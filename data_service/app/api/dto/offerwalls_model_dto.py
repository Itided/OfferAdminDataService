from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig
from app.models import OfferWall


class OfferWallDTO(SQLAlchemyDTO[OfferWall]): ...


class ReadOfferWallDTO(OfferWallDTO):
    config = DTOConfig(
        exclude={
            "offer_assignments.0.id",
            "offer_assignments.0.offer_wall_id",
            "offer_assignments.0.offer_id",
            "offer_assignments.0.offer_wall",
            "offer_assignments.0.order",
            "popup_assignments.0.id",
            "popup_assignments.0.offer_wall_id",
            "popup_assignments.0.offer_id",
            "popup_assignments.0.offer_wall",
            "popup_assignments.0.order",
        },
        max_nested_depth=2,
    )
