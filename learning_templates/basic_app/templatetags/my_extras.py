from django import template

register = template.Library()

def cut(value,args):
    """
    This cuts out all values of args from string
    """

    return value.replace(arg,'')

register.filter('cut',cut)
