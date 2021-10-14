from django import template

register = template.Library()

@register.filter(name='post_id_list')
def post_id_list(data):
    ls = [i.id for i in data]
    return ls

@register.filter(name='post_id_list1')
def post_id_list1(data):
    ls = [i.post.id for i in data]
    return ls