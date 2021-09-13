from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.views import View
from api.models import *
from .selenium_script import getGames



class GetPlayStoreGames(View):

    def get(self, request, *args, **kwargs):
        querySet = PlayStoreGamesCategory.objects.all()
        getGames(querySet)
        return HttpResponse('Done scraping playstore')