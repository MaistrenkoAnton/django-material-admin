import re

from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row
from django.contrib.admin.templatetags.base import InclusionAdminNode
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
    if 'request' not in context:
        return False
    request = context['request']
    result = request.COOKIES.get(cookie_name)
    return result == 'true'


@register.tag(name='additional_submit_row')
def additional_submit_row_tag(parser, token):
    return InclusionAdminNode(parser, token, func=submit_row, template_name='additional_submit_line.html')
