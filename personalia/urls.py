from django.conf.urls import url
from . import views

app_name = 'personalia'
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^menu/(?P<menu_id>[0-9]+)/$',views.menuShow, name='menuShow'),
    url(r'^action/(?P<action_id>[0-9]+)/(?P<params>[0-9]+)/$',views.actionShow, name='actionShow'),
]
