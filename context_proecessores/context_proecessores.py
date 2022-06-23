from post_app.models import post, categories



def recent(request):
    recent = post.objects.order_by("-author")

    return {"recent": recent}

def categore(request):
    categore = categories.objects.all()

    return {"categore": categore}