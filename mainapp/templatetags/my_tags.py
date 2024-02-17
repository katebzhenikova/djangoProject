from django import template

register = template.Library()


@register.filter()
def get_image(product):
    if product.product_image:
        return product.product_image.url
    else:
        return f'/media/products/no_photo.png'
