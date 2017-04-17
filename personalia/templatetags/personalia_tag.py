from django import template
from ..models import Menu

register = template.Library()

@register.inclusion_tag('personalia/menu.html')
def list_menu():
    menu_list = Menu.menu_show.all()
    return {'menu_list':menu_list,}
