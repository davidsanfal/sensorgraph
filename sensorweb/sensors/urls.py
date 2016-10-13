from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_csv_form),
    url(r'^graph/$', views.graph),
    ]
