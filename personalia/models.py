# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

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
    templatesource = models.CharField(max_length=250,default='personalia/index.html')
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
    templatesource = models.CharField(max_length=250,default='personalia/index.html')
    query_function = models.CharField(max_length=20,default='GetIndex')
    is_direct = models.BooleanField(default=True)

    class Meta:
        ordering = ('menu_id','action_order',)

    def __str__(self):
        return self.action_name

class Person(models.Model):
    GRADUATE_CHOICE = [
        ('1','SD'),('2','SMP'),('3','SMA'),('4','D3'),('5','S1'),
    ]
    GENDER_CHOICES = [
        ('L','Laki-laki'),('P','Perempuan'),
    ]
    STATUS_CHOICES = [
        ('1','Lajang'),('2','Menikah'),('3','Janda/Duda'),
    ]

    name = models.CharField(max_length=50)
    birthplace = models.CharField(max_length=15)
    birth = models.DateField()#(help_text='format is mm/dd/yyyy exmp:02/28/2000')
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,
        default='L')
    address = models.TextField(max_length=200)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,
        default='1')
    school = models.CharField(max_length=50)
    graduate = models.CharField(max_length=3,
        choices=GRADUATE_CHOICE,default='1')
    mobilephone = models.CharField(max_length=15)
    bbm = models.CharField(max_length=8,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)

    class Meta:
        ordering = ('gender','name','birth',)
        unique_together = ('name','birth','gender','email',)

    def __str__(self): # __unicode__ on Python 2
        return '{}-{}'.format(str(self.id),self.name)

class Leader(models.Model):
    MANAGER_CHOICES = [
        ('ahm','ahmad'),('ksm','kusmawan'),('mgd','migud'),
        ('sdk','sodikin'),('sdr','sodirun'),
    ]

    leader_id = models.CharField(max_length=5,primary_key=True,)
    name = models.CharField(max_length=50)
    manager = models.CharField(max_length=5,choices=MANAGER_CHOICES)

    class Meta:
        ordering = ('manager','leader_id',)

    def __str__(self):
        return self.name

class EmployeeReport(models.Manager):
    def Emp(self,condition):
        from django.db import connection as con
        with con.cursor() as cursor:
            cursor.execute('''
                select e.grade,p.gender,count(p.id) as counter
                from personalia_employee e
                inner join personalia_person p on e.person_id = p.id
                where %s
                group by e.grade,p.gender
                order by e.grade
            ''' % (condition,))
            result_list = []
            for row in cursor.fetchall():
                result_list.append(row)
        return result_list

class Employee(models.Model):
    LEVEL_CHOICES = [
        ('0','WB'),('1','Pra A1'),('2','A1_1'),('3','A1_2'),('4','A1_3'),('5','A2_a'),
        ('6','A2_b'),
    ]

    SA_CHOICES = [
        ('ak','AK'),('pa','PA'),('bk1','BK_1'),('bk2','BK_2'),('bk3','BK_3')
    ]
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    grade = models.CharField(max_length=1,
        choices=LEVEL_CHOICES)
    date_register = models.DateField(blank=True,null=True)
    status_active = models.CharField(max_length=5,choices=SA_CHOICES)
    leader = models.ForeignKey(Leader, related_name='LeaderOf')
    description = models.TextField(max_length=500,blank=True,null=True)

    objects = models.Manager()
    emp_report = EmployeeReport()

    class Meta:
        ordering = ('status_active','grade','person',)

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.person)

class Report(models.Model):
    report_name = models.CharField(max_length=200)
    script_name = models.CharField(max_length=200)
    group_report = models.CharField(max_length=10)
    is_enable = models.BooleanField(default=True)

    class Meta:
        ordering = ('report_name',)

class Coaching(models.Model):
    employee = models.ForeignKey(Employee, related_name='empOf')
    course = models.CharField(max_length=100)
    date_coaching = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=500,blank=True,null=True)

    class Meta:
        ordering = ('id',)
