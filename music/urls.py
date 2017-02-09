from django.conf.urls import url
from . import views     #i.e. from current directory, import views

#File contains url following the pattern "/music/*"
urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    #/music/album_id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = "detail"),
]