from django.conf.urls import url
from . import views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Main/', views.Main, name='Main'),
    url(r'^Login/', views.Login, name='Login'),
    url(r'^Widget/', views.Widget, name='Widget'),
    url(r'^Chart/', views.Chart, name='Chart'),
]