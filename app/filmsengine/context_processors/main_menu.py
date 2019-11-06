from django.template.context_processors import request
from films.models import Genre, Year


def menu(request):
    genres_list = Genre.objects.filter(status=True)
    year_list = Year.objects.all()
    return {'genres_list': genres_list,
            'year_list': year_list
            }
