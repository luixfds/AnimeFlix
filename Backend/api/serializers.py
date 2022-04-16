from rest_framework import serializers
from .models import *

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class AnimeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

class SeasonGroupSerializer (serializers.ModelSerializer):
    class Meta:
        model = SeasonGroup
        fields = '__all__'

class EpsGroupSerializer (serializers.ModelSerializer):
    class Meta:
        model = EpsGroup
        fields = '__all__'

class EpisodeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'
