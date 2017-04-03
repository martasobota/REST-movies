from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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

