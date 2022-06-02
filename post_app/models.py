import django.utils.timezone
from django.contrib.auth.models import User
from django.db import models




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

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(categories)
    tite = models.CharField(max_length=100, unique_for_date="pub_deta")
    bode = models.TextField()
    image = models.ImageField(upload_to="image")
    tima = models.DateTimeField(auto_now_add=True)
    updeta = models.DateTimeField(auto_now=True)
    pub_deta = models.DateField(default=django.utils.timezone.now)
    file_deta = models.FileField(upload_to="file deta", null=True, blank=True)
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    objects = models.Manager()
    costom_manger = Manager()


    def __str__(self):
        return f"{self.tite}, {self.bode[:20]}"



# save my views metod title bodey save int,str

# def save(self, *args, **kwargs):
# print("hi user")
# super(post, self).save(args, kwargs)

# name models in objects user

# author = models.ForeignKey(User, on_delete=models.CASCADE)
# author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="1")
# author = models.ForeignKey(User, on_delete=models.PROTECT)
# author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

