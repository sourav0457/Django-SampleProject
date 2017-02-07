from django.conf.urls import url
from . import views     #i.e. from current directory, import views

#File contains url following the pattern "/music/*"
urlpatterns = [
    url(r'^$', views.index, name='index'),
]