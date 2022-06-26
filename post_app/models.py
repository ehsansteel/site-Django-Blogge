import django.utils.timezone
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# name models feld

# null=True
# blank=True
# help_text="hi user"
# unique=True
# db_column="Edit name"
# editable=True
# choices=The parameter detects
# default=The parameter detects
# CHOICES = (
#         ('A', "django"),
#         ('B', "python"),
#         ('C', "ehsan"),
#         ('C', "amir"),
#         ('D', "ail"),
#         ('G', "user"),
#         ('F', "name"),
#         ('H', "admin"),
#     )



class categories(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# views
# model manger&
# class manger object all()
# aurthor object

class Manager(models.Manager):
    def get_costum(self):
        return super(Manager, self).get_costum().filter(status=True)


class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ManyToManyField(categories, related_name="posts")
    title = models.CharField(max_length=100, unique_for_date="pub_deta")
    bode = models.TextField()
    image = models.ImageField(upload_to="image")
    tima = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    pub_deta = models.DateField(default=django.utils.timezone.now)
    file_deta = models.FileField(upload_to="file deta", null=True, blank=True)
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    objects = models.Manager()
    costom_manger = Manager()



    def save(
        self, force_insert=False, force_update=False,
            using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(post, self).save()


    def get_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})


    def __str__(self):
        return f"{self.title}, {self.bode[:20]}"







# name models in objects user

# author = models.ForeignKey(User, on_delete=models.CASCADE)
# author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")
# author = models.ForeignKey(User, on_delete=models.PROTECT)
# author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

