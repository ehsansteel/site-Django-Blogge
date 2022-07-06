from django.shortcuts import render, get_object_or_404, redirect
from post_app.models import post, categories, comment
from django.core.paginator import Paginator
from .forms import ContactUsForms

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


# search box
def search(request):
    q = request.GET.get("q")
    aurthor = post.objects.filter(title__icontains=q)
    page_number = request.GET.get("page")
    paginator = Paginator(aurthor, 1)
    object_list = paginator.get_page(page_number)
    return render(request, "blog_app/articles_list.html", {"aurthor": object_list})

# forms.py
def contact(request):
    if request.method == "POST":
        form = ContactUsForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("heme:heme")

    form = ContactUsForms
    return render(request, "blog_app/contact.html", {"form": form})
