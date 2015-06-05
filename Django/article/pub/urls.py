from django.conf.urls import patterns, include, url
from django.conf.urls import *
from rest_framework import routers
from pub import views

router=routers.DefaultRouter()

urlpatterns = patterns('pub.views',
                       url(r'^$', 'index'),
                       url(r'^(?P<pub_id>\d+)/$', 'detail'),
                       url(r'^/(?P<poll_id>\d+)/results/$',
                           'results'),
                       url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
                       )
