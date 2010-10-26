from django.conf.urls.defaults import *
from tease.models import TeaserList

urlpatterns = patterns('tease.views',
    url(r'^$', 'staff_object_list',
        { 'queryset': TeaserList.objects.all() },
        name="teaserlists"),
    url(r'^list/(?P<slug>[\-\d\w]+)/$', 'staff_object_detail',
        { 'slug_field':'slug', 'queryset': TeaserList.objects.all() },
        name="teaserlist"),
    url(r'^load-feed/(?P<slug>[\-\d\w]+)/$', 'teaserlist_load_feed',
        {},
        name="teaserlist-load-feed"),
)
