from django import template

register = template.Library()

@register.filter(name='post_id_list')
def post_id_list(data):
    ls = [i.id for i in data]
    return ls