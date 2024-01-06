from django import template
from ..models import Animal

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(id=key.id)