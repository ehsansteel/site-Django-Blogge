from django.urls import path
from . import views


app_name = "assets"
urlpatterns = [
    path("", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
    path("register/", views.regester, name='register'),
    path("profile/", views.profile_Edit, name='EditProFile')
]
