from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .utils import *
from .forms import ContactForm
from .models import *


def index(request):
    movies = Movie.objects.filter(status_watched=True).order_by('-date_pub')[:12]
    return render(request, 'films/index.html',
                  context={'movies': movies})


def video(request, slug):
    obj = get_object_or_404(Movie, slug__iexact=slug, status_watched=True)
    obj.views += 1
    obj.save()
    # print(obj.genres.all())
    simular_movie = Movie.objects.filter(genres__in=obj.genres.all()).order_by('-views').exclude(id=obj.id).distinct()[
                    :3]
    new_movie = Movie.objects.all()[:6]
    popular_movies = Movie.objects.all().order_by('-views')[:6]
    # print(simular_ganres_movie)
    return render(request, 'films/video.html',
                  context={'movie': obj,
                           'simular_movie': simular_movie,
                           'new_movie': new_movie,
                           'popular_movies': popular_movies}
                  )


def popular_movies_list(request):
    title = 'Popular Movies'
    obj = Movie.objects.all().order_by('-views')
    get_page = request.GET.get('page')
    item_pages = 12
    context = PaginatorMixin(obj, item_pages, get_page).queryset_paginated()
    context.update({'title': title})
    return render(request, 'films/all_movies.html',
                  context=context
                  )


def movies_genres_list(request, name):
    title = 'genres {} movies'.format(name)
    obj = Movie.objects.filter(genres__name=name)
    get_page = request.GET.get('page')
    item_pages = 12
    context = PaginatorMixin(obj, item_pages, get_page).queryset_paginated()
    context.update({'title': title})
    return render(request, 'films/all_movies.html',
                  context=context
                  )


def movies_year_list(request, years):
    title = '{} movies'.format(years)
    obj = Movie.objects.filter(year__years=years)
    get_page = request.GET.get('page')
    item_pages = 12
    context = PaginatorMixin(obj, item_pages, get_page).queryset_paginated()
    context.update({'title': title})
    return render(request, 'films/all_movies.html',
                  context=context
                  )


def movies_all_list(request):
    title = 'new movies'
    obj = Movie.objects.all()
    get_page = request.GET.get('page')
    item_pages = 12
    context = PaginatorMixin(obj, item_pages, get_page).queryset_paginated()
    context.update({'title': title})
    return render(request, 'films/all_movies.html', context=context)


def director(request, slug):
    title = 'Movies directed by {}'.format(slug)
    obj = Movie.objects.filter(directors__slug=slug)
    get_page = request.GET.get('page')
    item_pages = 12
    context = PaginatorMixin(obj, item_pages, get_page).queryset_paginated()
    context.update({'title': title})
    return render(request, 'films/all_movies.html', context=context)


def actor(request, slug):
    obj = Movie.objects.filter(stars__slug=slug)
    print(obj)
    title = 'Movies actor {}'.format(slug)
    get_page = request.GET.get('page')
    item_pages = 12
    context = PaginatorMixin(obj, item_pages, get_page).queryset_paginated()
    context.update({'title': title})
    return render(request, 'films/all_movies.html', context=context)


def movies_search_list(request):
    search_query = request.GET.get('search', '')
    obj = Movie.objects.filter(Q(title__icontains=search_query) |
                               Q(description__icontains=search_query))

    title = 'Movies search {}'.format(search_query)
    get_page = request.GET.get('page')
    item_pages = 12
    context = PaginatorMixin(obj, item_pages, get_page).queryset_paginated()
    context.update({'title': title})
    context.update({'query': search_query})
    return render(request, 'films/search.html', context=context)


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['example@example.com'])
            form.save()
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()
    return render(request, 'films/contact_us.html', {'form': form})


def dmca(request):
    return render(request, 'films/dmca.html')


def privacy(request):
    return render(request, 'films/privacy.html')