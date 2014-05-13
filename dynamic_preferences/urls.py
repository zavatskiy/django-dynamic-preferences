from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

from dynamic_preferences import site_preferences, user_preferences, global_preferences
global_preferences.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dynamic_preferences.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()