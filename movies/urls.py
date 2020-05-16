from django.urls import path
from . import views

# all urls start with "movies/", this is defined in vidly.urls
# url configuration: define path objects that map url endpoints to view functions

app_name = 'movies' # then we can use movies:detail in index.html

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]