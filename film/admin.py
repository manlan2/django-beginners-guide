from django.contrib import admin

# Register your models here.
from .models import Actor, Category, Film, FilmActor, FilmCategory, Language,Country


class ActorAdmin(admin.ModelAdmin):
    search_fields = ('actor_id', 'first_name','last_name')
    list_display = ('actor_id', 'first_name','last_name', 'last_update',)

class FilmActorAdmin(admin.ModelAdmin):
    list_display = ('actor_id', 'film_id', 'last_update',)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country', 'last_updated',)

admin.site.register(Actor, ActorAdmin)
admin.site.register(Country, CountryAdmin)
# admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Film)
# admin.site.register(FilmActor)
admin.site.register(FilmActor, FilmActorAdmin)
admin.site.register(FilmCategory)
admin.site.register(Language)
