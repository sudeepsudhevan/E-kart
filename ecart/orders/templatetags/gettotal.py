from django import template

register = template.Library()


@register.simple_tag(name="gettotal")
def gettotal(cart, tax_rate):
    total = 0
    for item in cart.added_items.all():
        total += item.quantity * item.product.price
    return round(total * (1 + tax_rate / 100))
