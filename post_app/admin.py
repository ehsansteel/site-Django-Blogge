from django.contrib import admin
from .models import post, categories, comment, Message_form_user




admin.site.register(categories)
admin.site.register(post)
admin.site.register(comment)
admin.site.register(Message_form_user)
