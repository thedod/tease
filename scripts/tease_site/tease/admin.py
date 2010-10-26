from tease.models import Teaser,TeaserList
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

## Teaser
class TeaserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title','description','teaser_list',
                       'author','org')
        }),
        (_('Design'), {
            'classes': ('ltr-field',),
            'fields': ('image_url', 'image_width', 'title_color','text_color','background_color')
        }),
        (_('Links'), {
            'classes': ('ltr-field',),
            'fields': ('link','author_link','org_link')
        }),
    )
    list_display=('__unicode__','teaser_list','author','org')
    list_editable=('teaser_list',)
    list_filter=('teaser_list',)
    search_fields = ('title','description','author','org','link')
    class Media:
        css = {
            'all': ('admin-extra.css','jPicker-1.1.2.css')
        }
        js=('js/jquery.js',
            'js/ui.core.js',
            'js/jpicker-1.1.2.js',
            'js/pickerize.js',
            'js/teaser-list-back-link.js')

admin.site.register(Teaser,TeaserAdmin)

## Teaser (inline)
class TeaserInline(admin.TabularInline):
    model = Teaser
    extra = 3
    exclude = ('description','link','author','author_link','org','org_link','image_url','image_width',
               'title_color','text_color','background_color')
    class Media:
        css = {
            'all': ('admin-extra.css',)
        }

## TeaserList
class TeaserListForm(forms.ModelForm):
    model = TeaserList
    class Media:
        css = {
            'all': ('admin-extra.css',)
        }
        js=('js/jquery.js',
            'js/ui.core.js',
            'js/ui.sortable.js',
            'js/sortable-last-inline.js',
            'js/teaser-edit-links.js')

class TeaserListAdmin(admin.ModelAdmin):
    form = TeaserListForm
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        (_('Advanced options'), {
            'classes': ('collapse','ltr-field',),
            'fields': ('slug','link', 'feed_url','feed_method')
        }),
    )
    list_display = ('title','slug','feed_url')
    search_fields = ('slug','__unicode__','link','feed_url')
    inlines = [TeaserInline]

admin.site.register(TeaserList,TeaserListAdmin)
