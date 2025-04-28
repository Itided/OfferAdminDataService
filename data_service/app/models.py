from __future__ import annotations

import uuid
from enum import Enum as PyEnum

from sqlalchemy import BigInteger
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates


class OfferChoices(str, PyEnum):
    Loanplus = "Loanplus"
    SgroshiCPA2 = "SgroshiCPA2"
    Novikredyty = "Novikredyty"
    TurboGroshi = "TurboGroshi"
    Crypsee = "Crypsee"
    Suncredit = "Suncredit"
    Lehko = "Lehko"
    Monto = "Monto"
    Limon = "Limon"
    Amigo = "Amigo"
    FirstCredit = "FirstCredit"
    Finsfera = "Finsfera"
    Pango = "Pango"
    Treba = "Treba"
    StarFin = "StarFin"
    BitCapital = "BitCapital"
    SgroshiCPL = "SgroshiCPL"
    LoviLave = "LoviLave"
    Prostocredit = "Prostocredit"
    Sloncredit = "Sloncredit"
    Clickcredit = "Clickcredit"
    Credos = "Credos"
    Dodam = "Dodam"
    SelfieCredit = "SelfieCredit"
    Egroshi = "Egroshi"
    Alexcredit = "Alexcredit"
    SgroshiCPA1 = "SgroshiCPA1"
    Tengo = "Tengo"
    Credit7 = "Credit7"
    Tpozyka = "Tpozyka"
    Creditkasa = "Creditkasa"
    Moneyveo = "Moneyveo"
    My_Credit = "MyCredit"
    Credit_Plus = "CreditPlus"
    Miloan = "Miloan"
    Avans = "AvansCredit"


class Base(DeclarativeBase): ...


class OfferWall(Base):
    __tablename__ = "admin_panel_offerwall"

    token: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    name: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(String(200), default=None)
    description: Mapped[str | None] = mapped_column(Text)

    offer_assignments: Mapped[list["OfferWallOffer"]] = relationship(
        back_populates="offer_wall"
    )
    popup_assignments: Mapped[list["OfferWallPopupOffer"]] = relationship(
        back_populates="offer_wall"
    )

    def __str__(self):
        return f"OfferWall {self.token}"


class Offer(Base):
    __tablename__ = "admin_panel_offer"

    uuid_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, name="uuid"
    )
    id: Mapped[int]
    url: Mapped[str | None] = mapped_column(String(200), default=None)
    is_active: Mapped[bool] = mapped_column(default=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    sum_to: Mapped[str | None] = mapped_column(String, default=None)
    term_to: Mapped[int | None] = mapped_column(default=None)
    percent_rate: Mapped[int | None] = mapped_column(default=None)

    wall_assignments: Mapped[list["OfferWallOffer"]] = relationship(
        back_populates="offer",
        cascade="all, delete-orphan",
        order_by="OfferWallOffer.order",
    )

    popup_assignments: Mapped[list["OfferWallPopupOffer"]] = relationship(
        back_populates="offer",
        cascade="all, delete-orphan",
        order_by="OfferWallPopupOffer.order",
    )

    def __str__(self) -> str:
        return self.name

    @validates("name")
    def validate_name(self, key, value):
        if value not in OfferChoices.__members__:
            raise ValueError(
                f"Invalid value for {key}: {value}. Must be one of {list(OfferChoices.__members__.keys())}."
            )
        return value


class OfferWallOffer(Base):
    __tablename__ = "admin_panel_offerwalloffer"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    offer_wall_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("admin_panel_offerwall.token", ondelete="CASCADE")
    )
    offer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("admin_panel_offer.uuid", ondelete="CASCADE")
    )
    order: Mapped[int] = mapped_column(default=0)

    offer_wall: Mapped["OfferWall"] = relationship(back_populates="offer_assignments")
    offer: Mapped[Offer] = relationship(back_populates="wall_assignments")


class OfferWallPopupOffer(Base):
    __tablename__ = "admin_panel_offerwallpopupoffer"
    __table_args__ = (
        UniqueConstraint(
            "offer_wall_id",
            "offer_id",
            name="admin_panel_offerwallpop_offer_wall_id_offer_id_cd31ac20_uniq",
        ),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    offer_wall_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("admin_panel_offerwall.token")
    )
    offer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("admin_panel_offer.uuid"))
    order: Mapped[int] = mapped_column(default=0)

    offer_wall: Mapped["OfferWall"] = relationship(back_populates="popup_assignments")
    offer: Mapped[Offer] = relationship(back_populates="popup_assignments")
