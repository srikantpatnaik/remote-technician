from django.conf.urls.defaults import patterns, include, url
from app.views import hello, current_datetime, my_homepage
from app.hour_ahead import hour_ahead
from app.min_ahead import min_ahead
from app.hello import hu
from temp_dt import current_date
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^hello/$', hello),
                       ('^time/$', current_datetime),
                       ('^$', my_homepage),
                       (r'^hour/(\d{1,2})/$', hour_ahead),
                       (r'^min/(\d{1,2})/$', min_ahead),
                       (r'^hu/(\s "sachin")/$', hu),
                       (r'^cur_dt/$', current_date)
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
