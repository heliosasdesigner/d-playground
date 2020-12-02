from django import template

register = template.Library()


# another way using decorators
@register.filter(name='cu')

def customtag_cut(value,arg):
    """
    This cuts out all values of 'arg' from the string
    """
    return value.replace(arg,'')


# register this filter, ({{ the name your wanna use for call}},{{ the function name }})
# one way to register the filter
#register.filter('cut',customtag_cut)

