import re

from django import template
from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()


CL_VALUE_RE = re.compile('value=\"([^"]*)\"')


@register.filter
def admin_change_list_value(result_checkbox_html):
    """Extract value from rendered admin list action checkbox."""
    value = CL_VALUE_RE.findall(result_checkbox_html)
    return value[0] if value else None


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
    request = context['request']
    result = request.COOKIES.get(cookie_name)
    return result == 'true'
