from django.shortcuts import render, get_object_or_404
from post_app.models import post, categories, comment
from django.core.paginator import Paginator

# comment user body
def post_datal(request, slug):
    aurthor = get_object_or_404(post, slug=slug)
    if request.method == 'POST':
        body = request.POST.get("body")
        parent = request.POST.get("parent_id")
        comment.objects.create(body=body, parent_id=parent, article=aurthor, user=request.user)

    return render(request, "blog_app/post.html", {"aurthor": aurthor})



def post_list(request):
    aurthor = post.objects.all()
    page_number = request.GET.get("page")
    paginator = Paginator(aurthor, 2)
    object_list = paginator.get_page(page_number)
    return render(request, "blog_app/articles_list.html", {"aurthor": object_list})



def category_detail(request, pk=None):
    category = get_object_or_404(categories, id=pk)
    aurthor = category.posts.all()
    return render(request, "blog_app/articles_list.html", {"aurthor": aurthor})
