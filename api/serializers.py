from rest_framework import serializers
from .models import *


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Games
        fields = ('title','category','details_link')