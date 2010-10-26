from django.core import urlresolvers
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.views.generic.list_detail import object_list,object_detail
from tease.models import Teaser,TeaserList

@user_passes_test(lambda u: u.is_staff)
def staff_object_list(*args, **kwargs):
    return object_list(*args, **kwargs)

@user_passes_test(lambda u: u.is_staff)
def staff_object_detail(*args, **kwargs):
    return object_detail(*args, **kwargs)


@permission_required('tease.delete_teaser')
def teaserlist_load_feed(request,slug):
    tl=get_object_or_404(TeaserList,slug=slug)
    tl.load_feed() # might return False, but no indication [yet?]
    return HttpResponseRedirect(urlresolvers.reverse('teaserlist', args=(tl.slug,))
)
