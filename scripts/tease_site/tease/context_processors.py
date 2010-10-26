from tease.models import TeaserList

def teaserlists(request):
    res={}
    for tl in TeaserList.objects.all():
      res[tl.slug]=tl
    return {'TEASERLISTS':res}
