from django.conf.urls import url

from . import views

app_name = 'ps1'

urlpatterns = [
    url(r'^$', views.ps1, name='ps1'),
]
