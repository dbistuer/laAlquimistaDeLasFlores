from django import template
register = template.Library()


@register.simple_tag
def language_swap(path,lang):
    elements = path.split('/')
    if elements[1] != lang:
        elements[1] = lang
    return '/'.join(elements)
