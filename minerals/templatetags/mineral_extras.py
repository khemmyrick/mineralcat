import re

from django import template

from minerals.models import Mineral

# mineral_extras

register = template.Library()

@register.filter('formula_markup')
def formula_markup(f_string):
    """Takes string from a formula attriubte, and adds sub tags."""
    # OOPS... turns out this is redundant.  The strings already have those.
    # They just need the safe filter.
    # This explains why I was getting double <sub> tags.
    l_list = re.findall(r'\d+', f_string)
    for l_item in l_list:
        new_item = '<sub>{}</sub>'.format(l_item)
        f_string = f_string.replace(l_item, new_item)
    return f_string
