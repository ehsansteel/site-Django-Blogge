from django.contrib import admin
from .models import post, categories, comment




admin.site.register(categories)
admin.site.register(post)
admin.site.register(comment)
