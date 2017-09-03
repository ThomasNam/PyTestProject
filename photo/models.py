from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from photo.fields import ThumbnailImageField

from django.contrib.auth.models import User

@python_2_unicode_compatible
class Album(models.Model) :
    name = models.CharField(max_length=50)

    description = models.CharField('One Line Description', max_length=100, blank=True)

    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url (self) :
        return reverse("photo:album_detail", args=(self.id, ))


@python_2_unicode_compatible
class Photo(models.Model) :
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=50)

    image = ThumbnailImageField(upload_to='photo/%Y/%m')

    description = models.TextField('Photo Description', blank=True)
    update_date = models.DateTimeField('Update date', auto_now_add=True)

    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url (self) :
        return reverse("photo:photo_detail", args=(self.id, ))



@python_2_unicode_compatible
class Publication(models.Model) :
    title = models.CharField(max_length=30)
    albums = models.ManyToManyField(Album)


@python_2_unicode_compatible
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

@python_2_unicode_compatible
class Restaurant(models.Model):
    place = models.OneToOneField(Place)

    name = models.CharField(max_length=80, default="DefRestName")

    services_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.name

