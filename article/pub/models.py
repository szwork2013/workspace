from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice


class Journal(models.Model):
    name = models.CharField(max_length=200, null=True)
    publisher = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    e_givenname = models.CharField(max_length=200,default='', null=True)
    e_surname = models.CharField(max_length=200,default='', null=True)
    j_givenname = models.CharField(max_length=200,default='', null=True)
    j_surname = models.CharField(max_length=200,default='', null=True)

    def __unicode__(self):
        return self.e_givenname


class Language(models.Model):
    label = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.label


class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    year = models.IntegerField(default=0,null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    month = models.CharField(max_length=200, null=True)
    journal = models.ForeignKey(
        Journal, blank=True, null=True, on_delete=models.SET_NULL)
    date = models.IntegerField(default=0, null=True)
    volume = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=200, null=True)
    page = models.CharField(max_length=200, null=True)
    authors = models.ManyToManyField(
        Author, blank=True, null=True)
    language = models.ForeignKey(
        Language, blank=True, null=True, on_delete=models.SET_NULL)
    check = models.BooleanField(default=0)

    def __unicode__(self):
        return self.title
