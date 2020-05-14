from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    output = ', '.join([m.title for m in movies])
    # # SELECT * FROM movies_movie WHERE rease_year=1985
    # movies = Movie.objects.filter(rease_year=1985)
    # # SELECT * FROM movies_movie WHERE id=1
    # movies = Movie.objects.get(id=1)
    return HttpResponse(output)
