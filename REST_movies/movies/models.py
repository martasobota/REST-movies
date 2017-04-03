from __future__ import unicode_literals

from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=128)
    
    def __str__(self):
        return "First name: {}, Last name: {}".format(self.first_name, self.last_name)


class Movie(models.Model):
	title = models.CharField(max_length=256)
	description = models.TextField()
	director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name = 'director')
	actors = models.ManyToManyField(Person, through='Role', related_name='starring')
	year = models.IntegerField()

	def __str__(self):
		return "Movie title: {}, director: {}, screenplay: {}, starring: {}, year: {}, rating: {}".format(self.title, self.director, self.screenplay, self.starring, self.year, self.ranking)


class Role(models.Model):
    movie = models.ForeignKey(Movie)
    person = models.ForeignKey(Person)
    role = models.CharField(max_length=128, null=True)
    
    def __str__(self):
        return "Role: {}".format(self.role)