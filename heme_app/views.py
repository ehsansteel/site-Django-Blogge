from django.shortcuts import render
from post_app.models import post

# filetr(models django db)
# model
# model Manager and object
# model filter(status=True)

def index(request):
    aurthor = post.objects.all()#Manager_request
    return render(request, "heme_app/index.html", {'aurthor': aurthor})

# aurthor = post.published
# aurthor = post.status
# aurthor = post.costom_manger.filter(status=True)
# aurthor = post.costom_manger.all()




