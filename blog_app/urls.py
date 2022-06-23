from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("<slug:slug>", views.post_datal, name="detail"),
    path('', views.post_list, name="article-list"),

]