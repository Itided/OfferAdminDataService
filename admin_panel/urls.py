from django.urls import path, include
from admin_panel.api.offer_walls import router as offer_wall_router

urlpatterns = [
    path("", include(offer_wall_router.urls)),
]
