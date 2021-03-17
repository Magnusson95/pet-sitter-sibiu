from django import template

# Creating custom template tags and filters
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(cost, quantity):
    return cost * quantity
