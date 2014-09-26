# encoding: utf-8
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# ---------------------------------------------------------------------
# Configuración de la base de datos
# ---------------------------------------------------------------------

USE_SENTRY = False
#BASE_URL = 'dptolicencias/'
#STATIC_ROOT = "/home/marcos/mde/static-content/"
LOGIN_REDIRECT_URL = 'admin/'
TEMPLATE_STRING_IF_INVALID = 'ERROR'
INTERNAL_IPS = []

#BASE_STATIC_URL = 'rrhh/licencias/' #'sub'

#STATIC_URL = '/{0}/static/'.format(BASE_STATIC_URL[:-1])

#MEDIA_URL = '{0}medios/'.format(BASE_STATIC_URL)
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '{0}admin/'.format(STATIC_URL)

