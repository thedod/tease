
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMIN_DISABLED = False

SITE_ID = 1

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Bangkok'

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = '*******************'
DATABASE_USER = '*******************'
DATABASE_PASSWORD = '*******************'

# Looking for a random string? Not creative enough?
# https://api.wordpress.org/secret-key/1.1/ :)
SECRET_KEY = '*******************'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = '/path/to/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://example.com/path/to/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/django-admin-media/'

DJANGO_APP_PREFIX = '/path/to/scripts/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    DJANGO_APP_PREFIX+'/templates',
    '/path/to/django/contrib/admin/templates',
)

LOCALE_PATHS = (
    DJANGO_APP_PREFIX+'locale',
)
