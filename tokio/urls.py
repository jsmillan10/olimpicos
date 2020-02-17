from django.conf.urls import url

from . import views

app_name = 'tokio'

urlpatterns = [
    url(r'^$', views.inicio, name='index')
    ]