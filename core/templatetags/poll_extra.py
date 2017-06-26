from django import template
from core.models import *
register = template.Library()
import re


@register.filter(name="cimg")
def cimg(value):
    if value.img.name != '':
        return value.img.name[4:]
    else:
        return ""