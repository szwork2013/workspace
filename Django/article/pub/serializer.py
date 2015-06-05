from rest_framework import serializers
from pub.models import Article,Author,Journal,Language
from django.contrib.auth.models import User

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Article
        fields=('id','title','year','city','country','month','journal','date','volume','number','page','aouthors','language','check')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields=('id','label')

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields=('id','name','publisher')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author('id','e_givenname','e_surname','j_givenname','j_surname')
        
