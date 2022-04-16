from django.contrib import admin
from api.models import *

@admin.register(Category)
class CategoryFormat(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Anime)
class AnimeFormat(admin.ModelAdmin):
    list_display = ('title', 'year', 'category', 'min_faixaE', )

@admin.register(SeasonGroup)
class SeasonGroupFormat(admin.ModelAdmin):
    list_display = ('anime', 'season', )

@admin.register(EpsGroup)
class EpsGroupFormat(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Episode)
class EpisodeFormat(admin.ModelAdmin):
    list_display = ('name', 'group', )