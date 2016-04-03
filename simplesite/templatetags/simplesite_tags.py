# *-* coding=utf-8 *-*
from django import template

from simplesite.models import Page


register = template.Library()

@register.assignment_tag
def get_header_list():
    """
    Returns a list of pages that belong to header
    """
    return Page.objects.filter(is_header=True)

@register.assignment_tag
def get_footer_list():
    """
    Returns a list of pages that belong to header
    """
    return Page.objects.filter(is_footer=True)