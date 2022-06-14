from django.shortcuts import render, get_object_or_404
from post_app.models import post



def post_datal(request, pk):
    aurthor = get_object_or_404(post, id=pk)


    return render(request, "blog_app/post.html", {"aurthor": aurthor})