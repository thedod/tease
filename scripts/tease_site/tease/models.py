from django.db import models
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _
import re, htmlentitydefs, feedparser

### Utilities

def entity_unescape(text):
   """Removes HTML or XML character references and entities from a text string.
      Based on code from Fredrik Lundh http://effbot.org/zone/re-sub.htm#unescape-html
   """
   def fixup(m):
      text = m.group(0)
      if text[:2] == "&#":
         # character reference
         try:
            if text[:3] == "&#x":
               return unichr(int(text[3:-1], 16))
            else:
               return unichr(int(text[2:-1]))
         except ValueError:
            return '?'
      else:
         # named entity
         try:
            return unichr(htmlentitydefs.name2codepoint[text[1:-1]])
         except KeyError:
            return '?'
   return re.sub("&#?\w+;", fixup, text)

FEED_METHOD_CHOICES=(
    ('RSS/Atom','RSS/Atom'), # use feedparser on the url
    # in the future we might have some JSON stuff here too
)

# all methods return an iterable of dict-like entries
# with values for title, link, and summary
FEED_METHODS={
    'RSS/Atom' : (lambda url: feedparser.parse(url).entries),
}

### TeaserList

class TeaserList(models.Model):
    title = models.CharField(_('Title'),max_length=64)
    slug=models.SlugField(_('Slug'),unique=True,
            help_text=_("Unique identifier for URL. Only letters, digits, and _. e.g. international_news_2010 or about"))
    link=models.URLField(_('Link'),null=True,blank=True)
    feed_url=models.URLField(_('Feed url'),null=True,blank=True,
            help_text=_("Optional url of automatic source for teaser"))
    feed_method = models.CharField(_('Feed method'),max_length=23,
            choices=FEED_METHOD_CHOICES,default=FEED_METHOD_CHOICES[0][0],
            help_text=_("If feed url is present - format of the feed"))

    class Meta:
        verbose_name = _('Teaser list')
        verbose_name_plural = _('Teaser lists')
        ordering = ('feed_url','title',)

    def __unicode__(self):
        if self.feed_url:
            return u'%s (%s)' % (self.title,self.feed_method)
        else:
            return self.title

    def has_feed(self):
        return self.feed_url and FEED_METHODS.has_key(self.feed_method)

    def load_feed(self):
        if not self.has_feed():
            return False
        # all methods return an iterable of dict-like entries
        entries=FEED_METHODS[self.feed_method](self.feed_url)
        self.teasers.all().delete() # take no prizona
        i=0
        for e in entries:
            i+=1
            Teaser(teaser_list=self, sort_order=i,
                title=entity_unescape(e.get('title')),
                description=e.get('description'),
                link=e.get('link')
            ).save()
        return True

### Teaser

class Teaser(models.Model):
    title = models.CharField(_('Title'),max_length=256)
    description = tinymce_models.HTMLField(_('Description'),blank=True)
    link=models.URLField(_('Link'),null=True,blank=True)
    teaser_list = models.ForeignKey(TeaserList,verbose_name=_('Belongs to list'),related_name='teasers',blank=False)
    sort_order=models.IntegerField(_('Drag to sort'),default=0)
    author = models.CharField(_('Author'),max_length=256,null=True,blank=True)
    author_link = models.URLField(_('Author link'),null=True,blank=True)
    org = models.CharField(_('Author org'),max_length=256,null=True,blank=True)
    org_link = models.URLField(_('Author org link'),null=True,blank=True)
    image_url = models.URLField(_('Image URL'),null=True,blank=True)
    image_width = models.IntegerField(_('Image width'),default=75)
    title_color = models.CharField(_('Title color'),max_length=8,null=True,blank=True)
    text_color = models.CharField(_('Text color'),max_length=8,null=True,blank=True)
    background_color = models.CharField(_('Background color'),max_length=8,null=True,blank=True,
            help_text=_("Pick colors. Empty field means default"))

    class Meta:
        verbose_name = _('Teaser')
        verbose_name_plural = _('Teasers')
        ordering = ('teaser_list','sort_order')

    def __unicode__(self):
        return self.title

    def get_duplicates(self):
        """ return other teasers with same link, unless they're in a feed TeaserList (i.e. not featured) """
        if not self.link:
            return []
        return Teaser.objects.filter(link=self.link).exclude(pk=self.pk).filter(teaser_list__feed_url='')
