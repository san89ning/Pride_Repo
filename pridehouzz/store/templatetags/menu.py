from django import template

from store.models import Category, Brand, Size

register = template.Library()

@register.inclusion_tag('core/menu.html')
def menu():
    category = Category.objects.all()

    return {'category': category}

@register.inclusion_tag('core/brand.html')
def brand():
    brand = Brand.objects.all()

    return {'brand': brand}

@register.inclusion_tag('core/size.html')
def size():
    size = Size.objects.all()

    return {'size': size}