from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.http import HttpResponseRedirect

import session_csrf
session_csrf.monkeypatch()

from attract.views import stock
from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    # Examples:
    # url(r'^$', 'attract.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),

    url(r'^polls/', include('polls.urls')),
    url(r'^stock/', include('stock.urls')),
    url(r'^$', lambda r: HttpResponseRedirect('stock/highchart/')),
)

if settings.DEBUG:
    urlpatterns += tuple(static(settings.STATIC_URL, view=serve, show_indexes=True))
