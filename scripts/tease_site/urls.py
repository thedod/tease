from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
try:
    from settings import ADMIN_DISABLED
except:
    ADMIN_DISABLED=False

if ADMIN_DISABLED:
    urlpatterns = patterns('',
        (r'^admin/', 'sitehelpers.views.admin_disabled'),
    )
else:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^admin/', include(admin.site.urls)),
        (r'^accounts/', include('socialauth.urls')),
        url(r'^login/$', 'socialauth.views.openid_login_page', name='login'),
        (r'^dashboard/', include('tease.urls')),
        (r'^admin/filebrowser/', include('filebrowser.urls')),
    )

urlpatterns += patterns('',
    (r'^tinymce/', include('tinymce.urls')),
    (r'^cheat/$','sitehelpers.views.show_url_patterns'),
)
