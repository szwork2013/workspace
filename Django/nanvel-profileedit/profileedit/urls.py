from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from profileedit.apps.accounts.api import router as accounts_router


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'profileedit.apps.accounts.views.profile', name='profile-page'),
    url(r'^api/', include(accounts_router.urls)),
    url(r'^upload/', 'profileedit.apps.accounts.views.upload_image', name='photo-upload'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)


handler500 = 'profileedit.apps.core.views.handler500'
handler404 = 'profileedit.apps.core.views.handler404'
