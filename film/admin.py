from django.contrib import admin

# Register your models here.
from .models import Actor, Category, Film, FilmActor, FilmCategory, Language


class ActorAdmin(admin.ModelAdmin):
    list_display = ('actor_id', 'last_name', 'last_update',)

class FilmActorAdmin(admin.ModelAdmin):
    list_display = ('actor_id', 'film_id', 'last_update',)

admin.site.register(Actor, ActorAdmin)
# admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Film)
# admin.site.register(FilmActor)
admin.site.register(FilmActor, FilmActorAdmin)
admin.site.register(FilmCategory)
admin.site.register(Language)
