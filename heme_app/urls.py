from django.urls import path
from . import views


app_name = 'heme'
urlpatterns = [
    path("", views.index, name='heme'),
    path("", views.sidebar, name="sidebar")
]