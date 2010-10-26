# Django settings for tease_site app.

# Import site-specific stuff (see ../site-specific-examples/tease_site folder)
from local_settings import *
from social_settings import *

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'he'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'tease.context_processors.teaserlists',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'openid_consumer.middleware.OpenIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'tease_site.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'socialauth',
    'openid_consumer',
    'sitehelpers',
    'filebrowser',
    'tinymce',
    'tease',
)

##### Check to see if django-filebrowser is installed
##try:
##    import filebrowser
##    INSTALLED_APPS += ('filebrowser',)
##    TINYMCE_FILEBROWSER = True
##except ImportError:
##    pass

TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False

TINYMCE_DEFAULT_CONFIG = {
    'debug': True,
    'theme': 'advanced',
    'plugins':'directionality,media',
    'theme_advanced_buttons1' : 'formatselect,bold,italic,removeformat,|,justifyleft,justifycenter,justifyright,rtl,ltr,|,link,unlink,|,image,media,charmap,|,undo,redo,cleanup,code',
    'theme_advanced_buttons2' : '',
    'theme_advanced_buttons3' : '',
    'relative_urls': False,
}
