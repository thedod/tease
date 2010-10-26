from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.utils.translation import check_for_language
from django.contrib.auth.decorators import user_passes_test

def _(s):
    "Dummy i18n function for voodoo reasons"
    return s

def admin_disabled(request):
   return render_to_response('admin-disabled.html', {}, context_instance=RequestContext(request))

# ============= /cheat ======================================
from django.core import urlresolvers
from django.http import HttpResponse

intro_text = """Named URL patterns for the {% url %} tag
========================================

e.g. {% url pattern-name %}
or   {% url pattern-name arg1 %} if the pattern requires arguments

"""
@user_passes_test(lambda u: u.is_staff)
def show_url_patterns(request):
    patterns = _get_named_patterns()
    r = HttpResponse(intro_text, content_type = 'text/plain')
    longest = max([len(pair[0]) for pair in patterns])
    for key, value in patterns:
        r.write('%s %s\n' % (key.ljust(longest + 1), value))
    return r

def _get_named_patterns():
    "Returns list of (pattern-name, pattern) tuples"
    resolver = urlresolvers.get_resolver(None)
    patterns = sorted([
        (key, value[0][0][0])
        for key, value in resolver.reverse_dict.items()
        if isinstance(key, basestring)
    ])
    return patterns

