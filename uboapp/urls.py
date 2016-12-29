from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.building_list, name='building_list'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^get_building/$', views.get_building, name='get_building'),
    url(r'^post_rating/$', views.post_rating, name='post_rating'),
]

