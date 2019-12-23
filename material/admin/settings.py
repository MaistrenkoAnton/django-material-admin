from django.conf import settings
try:
    from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles  # Django2 support
except ImportError:
    from django.templatetags.static import static as staticfiles

try:
    settings = settings.MATERIAL_ADMIN_SITE
except AttributeError:
    settings = {}


def _get_setting(setting_name):
    return settings.get(setting_name) and settings[setting_name]


def _get_setting_static(setting_name):
    return settings.get(setting_name) and staticfiles(settings[setting_name])


MATERIAL_ADMIN_SITE = {
    'HEADER':  _get_setting('HEADER'),
    'TITLE':  _get_setting('TITLE'),
    'FAVICON':  _get_setting_static('FAVICON'),
    'MAIN_BG_COLOR':  _get_setting('MAIN_BG_COLOR'),
    'MAIN_HOVER_COLOR':  _get_setting('MAIN_HOVER_COLOR'),
    'PROFILE_PICTURE':  _get_setting_static('PROFILE_PICTURE'),
    'PROFILE_BG':  _get_setting_static('PROFILE_BG'),
    'LOGIN_LOGO':  _get_setting_static('LOGIN_LOGO'),
    'LOGOUT_BG':  _get_setting_static('LOGOUT_BG'),
    'SHOW_THEMES':  _get_setting('SHOW_THEMES'),
    'TRAY_REVERSE':  _get_setting('TRAY_REVERSE'),
    'NAVBAR_REVERSE':  _get_setting('NAVBAR_REVERSE'),
    'SHOW_COUNTS':  _get_setting('SHOW_COUNTS'),
    'APP_ICONS': {
        'auth': 'group',
        'sites': 'web'
    },
    'MODEL_ICONS': {
        'user': 'person',
        'group': 'people',
        'site': 'web',
    }
}

MATERIAL_ADMIN_SITE['APP_ICONS'].update(_get_setting('APP_ICONS') or {})
MATERIAL_ADMIN_SITE['MODEL_ICONS'].update(_get_setting('MODEL_ICONS') or {})
