from .models import Person, Movie, Role
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Person
		fields = ('first_name', 'last_name')

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ('title', 'description', 'director', 'actors', 'year')

class RoleSerializer(serializers.ModelSerializer):
	model = Role
	fields = ('movie', 'person', 'role')


