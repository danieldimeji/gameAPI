from django.urls import path
from .views import *

urlpatterns = [
 
    path('playstore/', GetPlayStoreGames.as_view(), name = 'playstore'),

]
