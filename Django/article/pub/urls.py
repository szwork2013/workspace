from django.conf.urls import patterns, include, url

urlpatterns = patterns('pub.views',
                       url(r'^$', 'index'),
                       url(r'^(?P<pub_id>\d+)/$', 'detail'),
                       url(r'^/(?P<poll_id>\d+)/results/$',
                           'results'),
                       url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
                       )
