import re

from django.template import Library
register = Library()


CL_VALUE_RE = re.compile('value=\"([^"]*)\"')


@register.filter
def admin_change_list_value(result_checkbox_html):
    """Extract value from rendered admin list action checkbox."""
    value = CL_VALUE_RE.findall(result_checkbox_html)
    return value[0] if value else None
