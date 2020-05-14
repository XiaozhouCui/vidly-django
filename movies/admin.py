from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    # hide the date_created field from admin interface
    exclude = ('date_created',)
    # display attributes columns instead of an object
    list_display = ('title', 'number_in_stock', 'daily_rate')

# Register your models here, so that they will be shown in the admin interface
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
