from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='Censor')
@stringfilter
def Censor(value):
    bad_words = ('mat', 'abc', 'gdgfdf', 'nsdfsdf', 'remarkable')
    if isinstance(value, str):
        words = value.split()
        for word in bad_words:
            value = value.replace(words, '*' * len(word))
    return value
