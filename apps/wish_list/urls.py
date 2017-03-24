from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^logout$', views.logout, name = 'my_logout'),
    url(r'^take', views.take, name = 'my_take'),
    url(r'^remove', views.remove, name = 'my_remove'),
    url(r'^add$', views.add, name = 'my_add'),
    url(r'^delete$', views.delete, name = 'my_delete'),
    url(r'^create$', views.create, name = 'my_create'),
    url(r'^wish_items/(?P<id>\d+)', views.items, name = 'my_items'),

]
