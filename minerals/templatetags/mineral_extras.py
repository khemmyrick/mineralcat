from django import template

from minerals.models import Mineral


register = template.Library()


@register.filter('underspace')
def underspace(attr_string):
    return attr_string.replace('_', ' ')
