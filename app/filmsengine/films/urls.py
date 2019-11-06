from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import MovieSitemap

sitemaps = {
    'items': MovieSitemap,
}

urlpatterns = [
    path('', views.index, name='index_url'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('video/<str:slug>', views.video, name='video_url'),
    path('movie/all/', views.movies_all_list, name='movies_all_url'),
    path('movie/search/', views.movies_search_list, name='movies_search'),
    path('movie/popular_movies/', views.popular_movies_list, name='popular_movies_url'),
    path('movie/genres/<str:name>', views.movies_genres_list, name='genres_url'),
    path('movie/year/<str:years>', views.movies_year_list, name='year_url'),
    path('director/<str:slug>', views.director, name='director_url'),
    path('actor/<str:slug>', views.actor, name='actor_url'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('dmca/', views.dmca, name='dmca'),
    path('privacy-policy/', views.privacy, name='privacy_policy'),
]
