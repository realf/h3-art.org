from h3_art import settings
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gifts import views as gifts_views
from users import views as users_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'h3_art.views.home', name='home'),
    # url(r'^h3_art/', include('h3_art.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', gifts_views.main),
    url(r'^gifts/new/([A-Za-z]*)$', gifts_views.new_gift),
    url(r'^gifts/$', gifts_views.user_gifts),
    url(r'^accounts/login/$', login, {'template_name':'login.html'}),
    url(r'^accounts/logout/$', logout, {'template_name':'logout.html'}),
    # User Profile
    url(r'^accounts/profile/$', users_views.user_profile),
    url(r'^accounts/profile/([0-9A-Za-z]*)$', gifts_views.user_profile),
    # User Registration
    url(r'^r/$', users_views.register),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
