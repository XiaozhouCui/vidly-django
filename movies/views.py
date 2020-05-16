from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.
def index(request):
    # SELECT * FROM movies_movie
    movies = Movie.objects.all()
    # # SELECT * FROM movies_movie WHERE rease_year=1985
    # movies = Movie.objects.filter(rease_year=1985)
    # # SELECT * FROM movies_movie WHERE id=1
    # movies = Movie.objects.get(id=1)
    # output = ', '.join([m.title for m in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', { 'movies': movies }) # use html template


def detail(request, movie_id):
    # try:
    #     movie = Movie.objects.get(pk=movie_id) # Movie class is defined in models.py 
    #     return render(request, 'movies/detail.html', { 'movie': movie })
    #     # return HttpResponse(movie_id)
    # except Movie.DoesNotExist:
    #     raise Http404() # 404 class is imported from django.http at the top

    # Movie class is defined in models.py
    movie =get_object_or_404(Movie, pk=movie_id) # no longer need the try catch blocks for 404
    return render(request, 'movies/detail.html', {'movie': movie})
