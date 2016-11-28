from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.building_list, name='building_list'),
    url(r'^create_post/$', views.create_post, name='create_post'),
]

