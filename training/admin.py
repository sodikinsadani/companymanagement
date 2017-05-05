from django.contrib import admin
from .models import Menu,Action

class actionAdmin(admin.ModelAdmin):
    list_display = ('menu_id','action_name','action_header','slug','is_enable','action_order','templatesource','query_function','is_direct')
    prepopulated_fields = {'slug':('menu_id','action_name')}

class menuAdmin(admin.ModelAdmin):
    list_display = ('menu_id','menu_parent','menu_type','menu_name','slug','is_active','is_act_view','menu_order','templatesource','query_function')
    prepopulated_fields = {'slug':('menu_id','menu_name')}

admin.site.register(Menu,menuAdmin)
admin.site.register(Action,actionAdmin)
