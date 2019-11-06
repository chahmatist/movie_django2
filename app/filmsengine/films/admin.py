from django.contrib import admin
from .models import Movie, Person, Genre

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Genre)