from django.conf.urls.defaults import patterns, include, url
from app.views import hello, current_datetime, my_homepage
from app.hour_ahead import hour_ahead
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^hello/$', hello),
                       ('^time/$', current_datetime),
                       ('^$', my_homepage),
                       (r'^ahead/(\d{1,2})/$', hour_ahead)
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
