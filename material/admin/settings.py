from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static as staticfiles


settings = settings.MATERIAL_ADMIN_SITE or {}


def _get_setting(setting_name):
    return settings.get(setting_name) and settings[setting_name]


def _get_setting_static(setting_name):
    return settings.get(setting_name) and staticfiles(settings[setting_name])


MATERIAL_ADMIN_SITE = {
    'HEADER':  _get_setting('HEADER'),
    'TITLE':  _get_setting('TITLE'),
    'FAVICON':  staticfiles('demo.png'),
    'MAIN_BG_COLOR':  _get_setting('MAIN_BG_COLOR'),
    'MAIN_HOVER_COLOR':  _get_setting('MAIN_HOVER_COLOR'),
    'PROFILE_PICTURE':  _get_setting_static('PROFILE_PICTURE'),
    'PROFILE_BG':  _get_setting_static('PROFILE_BG'),
    'LOGIN_LOGO':  _get_setting_static('LOGIN_LOGO'),
    'LOGOUT_BG':  _get_setting_static('LOGOUT_BG'),
    'SHOW_THEMES':  _get_setting('SHOW_THEMES'),
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
