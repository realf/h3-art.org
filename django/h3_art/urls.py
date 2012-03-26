from django.conf.urls import patterns, include, url
from gifts import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'h3_art.views.home', name='home'),
    # url(r'^h3_art/', include('h3_art.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^gifts/$', views.user_gifts),
    url(r'^gifts/new/$', views.new_gift),
)
