from django.urls import path
from .views import *

urlpatterns = [
    path("Anime/", Anime_API.as_view(), name='Anime'),
    path('Anime/<int:pk>/', Anime_API.as_view(), name='AnimeParameters'),
    
    path("Category/", Category_API.as_view(), name='Category'),
    path('Category/<int:pk>/', Category_API.as_view(), name='CategoryParameters'),
    
    path("SeasonGroup/", SeasonGroup_API.as_view(), name='SeasonGroup'),
    path('SeasonGroup/<int:pk>/', SeasonGroup_API.as_view(), name='SeasonGroupParameters'),
    
    path("EpsGroup/", EpsGroup_API.as_view(), name='EpsGroup'),
    path('EpsGroup/<int:pk>/', EpsGroup_API.as_view(), name='EpsGroupParameters'),
    
    path("Episode/", Episode_API.as_view(), name='Episode'),
    path('Episode/<int:pk>/', Episode_API.as_view(), name='EpisodeParameters'),
]