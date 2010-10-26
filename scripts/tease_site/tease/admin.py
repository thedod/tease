from tease.models import Teaser,TeaserList
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

## Teaser
class TeaserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title','link','description','teaser_list')
        }),
        (_('Design'), {
            'fields': ('image_url', 'image_width')
        }),
    )
    list_display=('__unicode__','teaser_list')
    list_editable=('teaser_list',)
    list_filter=('teaser_list',)
    search_fields = ('title','description')
    class Media:
        css = {
            'all': ('admin-extra.css',) # 'jPicker-1.1.2.css')
        }
        js=('js/jquery.js',
            'js/ui.core.js',
            # Not used at the moment. For color-picker
            #'js/jpicker-1.1.2.js',
            #'js/pickerize.js',
            'js/teaser-list-back-link.js')

admin.site.register(Teaser,TeaserAdmin)

## Teaser (inline)
class TeaserInline(admin.TabularInline):
    model = Teaser
    extra = 3
    exclude = ('description','link','image_url','image_width')
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
