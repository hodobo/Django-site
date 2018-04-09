from django.contrib import admin
from .models import BaiJie, Movie


class BaijieAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    ordering = ['publish']


class MovieAdmin(admin.ModelAdmin):
    list_display = ("movie", "movie_url", "image_url")


admin.site.register(Movie, MovieAdmin)
admin.site.register(BaiJie, BaijieAdmin)

# Register your models here.
