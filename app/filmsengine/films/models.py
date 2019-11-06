from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Genre(models.Model):
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genres_url', kwargs={'name': self.name})


class Person(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url_director(self):
        return reverse('director_url', kwargs={'slug': self.slug})

    def get_absolute_url_actor(self):
        return reverse('actor_url', kwargs={'slug': self.slug})


class Seasone(models.Model):
    name = models.CharField(max_length=255)
    episodes = models.ManyToManyField('Episode', blank=True, related_name='episodes')


class Episode(models.Model):
    name = models.CharField(max_length=255)


class Link(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Year(models.Model):
    years = models.SmallIntegerField(default='2019', db_index=True, unique=True)

    def __str__(self):
        return str(self.years)

    def get_absolute_url(self):
        return reverse('year_url', kwargs={'years': self.years})


class Movie(models.Model):
    title = models.CharField(max_length=150, db_index=True, unique=True)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    description = models.TextField(blank=True)
    status_watched = models.BooleanField(default=True)
    banner = models.CharField(max_length=150, null=True, blank=True)
    imbdID = models.CharField(max_length=50, null=True, blank=True)
    release = models.DateTimeField(null=True,)
    genres = models.ManyToManyField(
        'Genre', related_name='genres'
    )
    directors = models.ManyToManyField(
        'Person', related_name='directors'
    )
    stars = models.ManyToManyField(
        'Person', related_name='stars'
    )
    links = models.ManyToManyField(
        'Link', related_name='links'
    )
    seasones = models.ManyToManyField(
        'Seasone', blank=True, related_name='seasone'
    )
    year = models.ForeignKey(
        Year, on_delete=models.CASCADE, related_name='year'
    )
    image = models.ImageField(upload_to='images/')
    views = models.PositiveIntegerField(default=0)
    # Quality
    # Keywords
    # Country

    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('video_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


class ContactAs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
