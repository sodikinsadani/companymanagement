# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Menu,Action,Leader,Person,Employee,Report

class actionAdmin(admin.ModelAdmin):
    list_display = ('menu_id','action_name','action_header','slug','is_enable','action_order','templatesource','query_function','is_direct')
    prepopulated_fields = {'slug':('menu_id','action_name')}

class menuAdmin(admin.ModelAdmin):
    list_display = ('menu_id','menu_parent','menu_type','menu_name','slug','is_active','is_act_view','menu_order','templatesource','query_function')
    prepopulated_fields = {'slug':('menu_id','menu_name')}

class leaderAdmin(admin.ModelAdmin):
    list_display = ('leader_id','name','manager')

class employeeAdmin(admin.ModelAdmin):
    list_display = ('person','grade','date_register','status_active','leader','description','date_input')

class personAdmin(admin.ModelAdmin):
    list_display = ('name','birthplace','birth','gender','address',
        'status','school','graduate','mobilephone','bbm','email',)

class reportAdmin(admin.ModelAdmin):
    list_display = ('report_name','script_name','group_report','is_enable')

admin.site.register(Menu,menuAdmin)
admin.site.register(Action,actionAdmin)
admin.site.register(Leader,leaderAdmin)
admin.site.register(Person,personAdmin)
admin.site.register(Employee,employeeAdmin)
admin.site.register(Report,reportAdmin)
