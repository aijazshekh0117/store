from django.urls import path, include

from .views import *


router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'bookview', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("", index, name="index"),
]