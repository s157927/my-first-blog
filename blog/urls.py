from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^examples/$', views.examples, name='examples'),
    url(r'^newUser/$', views.newUser, name='newUser'),
    url(r'^discover/$', views.discover, name='discover'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

]
