from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie

from .serializers import MovieSerializer

# Create your views here.

class MoviesView(APIView):

	def get_all(self):
		try:
			return Movie.objects.all()
		except Movie.DoesNotExist:
			raise Http404

	def get(self, request, format=None):
		movies = Movie.objects.all()
		serializer = MovieSerializer(movies, many=True, context={'request':request})
		return Response(serializer.data)

class MovieView(APIView):

	def get_object(self, pk):
		try:
			return Movie.objects.get(pk=pk)
		except Movie.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		movie = self.get_object(id)
		serializer = MovieSerializer(movie, context={'request':request})
		return Response(serializer.data)

	def delete(self, request, id, format=None):
		movie = self.get_object(id)
		movie.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, id, format=None):
		movie = self.get_object(id)
		serializer = MovieSerializer(movie, context={'request':request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data

		return Response(serializer.errors, status=statu.HTTP_400_BAD_REQUEST)
