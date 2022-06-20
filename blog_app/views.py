from django.shortcuts import render, get_object_or_404
from post_app.models import post



def post_datal(request, slug):
    aurthor = get_object_or_404(post, slug=slug)


    return render(request, "blog_app/post.html", {"aurthor": aurthor})


def post_list(request):
    aurthor = post.objects.all()
    return render(request, "blog_app/articles_list.html", {"aurthor": aurthor})