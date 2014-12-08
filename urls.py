from django.conf.urls.defaults import *
from mysite.views import hello,current_datetime, hours_ahead, display_meta
from mysite.books import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^hello/$', hello),
    (r'^meta/$', display_meta),
    #(r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^contact/$', views.contact),
    #(r'^admin/', include(admin.site.urls)),
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
