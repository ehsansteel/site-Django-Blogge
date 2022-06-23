from django.shortcuts import render
from post_app.models import post

# filetr(models django db)
# model
# model Manager and object
# model filter(status=True)

def index(request):
    aurthor = post.objects.all()#Manager_request
    recent_articles = post.objects.all().order_by('-update', '-tima')
    return render(request, "heme_app/index.html", {'aurthor': aurthor, "recent_articles": recent_articles})



def sidebar(request):
    date = {"name": "EhsanFouladi"}
    return render(request, "includes/sidebar.html", context=date)




# aurthor = post.published
# aurthor = post.status
# aurthor = post.costom_manger.filter(status=True)
# aurthor = post.costom_manger.all()




