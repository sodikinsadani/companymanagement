from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from personalia.models import Employee

class MenuManager(models.Manager):
    def get_queryset(self):
        return super(MenuManager,
            self).get_queryset().filter(is_active=True)

class Menu(models.Model):
    MENUTYPE_CHOICE = [
        ('g','Group'),('p','Page'),
    ]

    menu_id = models.CharField(max_length=6,primary_key=True)
    menu_parent = models.CharField(max_length=6,default='000000')
    menu_type = models.CharField(max_length=1,
        choices=MENUTYPE_CHOICE,default='g'
    )
    menu_name = models.CharField(max_length=250,default='menu')
    slug = models.SlugField(max_length=250,
        unique=menu_id,blank=True)
    is_active = models.BooleanField(default=True)
    is_act_view = models.BooleanField(default=True)
    menu_order = models.IntegerField()
    templatesource = models.CharField(max_length=250,default='training/index.html')
    query_function = models.CharField(max_length=20,default='GetIndex')

    objects = models.Manager()
    menu_show = MenuManager()

    class Meta:
        ordering = ('menu_parent','menu_order',)

    def __str__(self):
        return self.menu_name

class Action(models.Model):
    menu_id = models.ForeignKey(Menu, related_name='actionMenu', on_delete=models.CASCADE)
    action_name = models.CharField(max_length=250,default='action')
    action_header = models.CharField(max_length=250,default='action')
    slug = models.SlugField(max_length=250,
        unique=id,blank=True)
    is_enable = models.BooleanField(default=True)
    action_order = models.IntegerField()
    templatesource = models.CharField(max_length=250,default='training/index.html')
    query_function = models.CharField(max_length=20,default='GetIndex')
    is_direct = models.BooleanField(default=True)

    class Meta:
        ordering = ('menu_id','action_order',)

    def __str__(self):
        return self.action_name

class Entrant(models.Model):
    member = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    status_active = models.BooleanField(default=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    date_input = models.DateTimeField(default=timezone.now)
