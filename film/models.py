# # coding:utf-8
from __future__ import unicode_literals

from django.db import models


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now=True)
    films = models.ManyToManyField('Film', through='FilmActor')

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'actor'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)
    films = models.ManyToManyField('Film', through='FilmCategory')

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        db_table = 'category'


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language')
    original_language = models.ForeignKey(
        'Language', blank=True, null=True,
        related_name='filmAsOriginalLanguage')
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    special_features = models.TextField(blank=True)
    fulltext = models.TextField()
    categories = models.ManyToManyField(Category, through='FilmCategory')
    actors = models.ManyToManyField(Actor, through='FilmActor')

    def __str__(self):
        return u'%s' % self.title

    class Meta:
        db_table = 'film'


# @python_2_unicode_compatible
class FilmActor(models.Model):
    actor = models.ForeignKey(Actor)
    film = models.ForeignKey(Film)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_actor'

    def __str__(self):
        return u'%s %s' % (self.film.title, self.actor.first_name)


class FilmCategory(models.Model):
    film = models.ForeignKey(Film)
    category = models.ForeignKey(Category)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'film_category'

    def __str__(self):
        return u'%s' % self.film.title

class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        db_table = 'language'

# CREATE TABLE IF NOT EXISTS "country" (
#   "country_id" smallint PRIMARY KEY NOT NULL,
#   "country" varchar(50) NOT NULL,
#   "last_update" timestamp
# );

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Country'

    def __str__(self):
        return u'%s' % self.country