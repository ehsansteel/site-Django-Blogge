from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("heme_app.urls", namespace="heme")),
    path("login/", include("login_app.urls", namespace="login")),
    path("register/", include("login_app.urls", namespace="register")),
    path("post/", include("blog_app.urls"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
