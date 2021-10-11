from django import template

register = template.Library()

@register.filter(name='list_safe')
def list_safe(data):
    print(data)
    return data