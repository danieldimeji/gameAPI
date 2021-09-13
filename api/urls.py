from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('games',views.GamesViewSet, basename='games')

urlpatterns = router.urls
