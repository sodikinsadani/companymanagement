from django import template
from training.models import Menu

register = template.Library()

@register.inclusion_tag('training/menu.html')
def list_menu():
    menu_list = Menu.menu_show.all()
    return {'menu_list':menu_list,}
