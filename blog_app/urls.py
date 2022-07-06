from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("<slug:slug>", views.post_datal, name="detail"),
    path('', views.post_list, name="article-list"),
    path("category/<int:pk>", views.category_detail, name="category_detail"),
    path("search/", views.search, name="search"),
    path("contact/", views.contact, name="contact_article")
]