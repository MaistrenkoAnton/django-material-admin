import json
import re
from json import JSONDecodeError

from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row
from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.contrib.admin.views.main import PAGE_VAR
from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from material.admin.settings import MATERIAL_ADMIN_SITE

register = Library()


CL_VALUE_RE = re.compile('value=\"([^"]*)\"')
CL_NAME_RE = re.compile('name=\"([^"]*)\"')
CHECK_CHECKBOX_TYPE = 'type="checkbox"'
DOT = '.'


@register.filter
def admin_change_list_value(result_checkbox_html):
    """Extract value from rendered admin list action checkbox."""
    value = CL_VALUE_RE.findall(result_checkbox_html)
    return value[0] if value else None


@register.filter
def admin_change_list_editable_checkbox(html):
    """Editable checkbox in admin list transform for materialize."""
    if CHECK_CHECKBOX_TYPE in html:
        name = CL_NAME_RE.findall(html)
        if name:
            checked = 'checked'
            if checked not in html:
                checked = ''
            field_name = name[0].split('-')[-1]
            return mark_safe("""<td class="field-{field_name}">
              <label for="id_{name}" class="checkbox-block">
                <input name="{name}" id="id_{name}" type="checkbox" {checked}>
                <span></span>
              </label>
            </td>""".format(field_name=field_name, name=name[0], checked=checked))
    return html


@register.filter
@stringfilter
def template_exists(value):
    try:
        template.loader.get_template(value)
        return True
    except template.TemplateDoesNotExist:
        return False


@register.simple_tag(takes_context=True)
def cookie(context, cookie_name):
    if 'request' not in context:
        return False

    def _is_cookie_reversed(setting, *cookies):
        return MATERIAL_ADMIN_SITE[setting] and cookie_name in cookies

    request = context['request']
    try:
        cookie_value = json.loads(request.COOKIES.get(cookie_name))
    except (JSONDecodeError, TypeError):
        cookie_value = False
    if _is_cookie_reversed('TRAY_REVERSE', 'additional-submit-line', 'object-tools') \
            or _is_cookie_reversed('NAVBAR_REVERSE', 'tray-nav-bar'):
        return not cookie_value
    return cookie_value


@register.simple_tag(takes_context=True)
def cookie_current_theme(context, preview):
    if preview:
        return preview
    if 'request' not in context:
        return 'default'
    request = context['request']
    return request.COOKIES.get('current_theme', 'default')


@register.tag(name='additional_submit_row')
def additional_submit_row_tag(parser, token):
    return InclusionAdminNode(parser, token, func=submit_row, template_name='additional_submit_line.html')


@register.simple_tag
def material_paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    if i == DOT:
        return '… '
    elif i == cl.page_num:
        return format_html('<li class="active"><a>{}</a></li></li> ', i)
    else:
        return format_html(
            '<li class="waves-effect"><a href="{}"{}>{}</a></li> ',
            cl.get_query_string({PAGE_VAR: i}),
            mark_safe(' class="end"' if i == cl.paginator.num_pages else ''),
            i,
        )
