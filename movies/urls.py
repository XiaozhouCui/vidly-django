from django.urls import path
from . import views

# movies/
# movies/1/details

# url configuration: define path objects that map url endpoints to view functions
urlpatterns = [
    path('', views.index, name='index')
]