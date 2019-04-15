from django.db import models
import os
from django.db.models import Q
import random
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.urls import reverse

def get_filename_ext(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name , ext

def upload_image_path(instance , filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1,397625012)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'
    

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True,active=True)

    def search(self, query):
        lookup = (Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(tag__title__icontains=query)
            )

        return self.filter(lookup).distinct()

class ProductManager(models.Manager):
    
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self.db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def search(self, query):
        return self.get_queryset().active().search(query)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class product(models.Model):
    title = models.CharField(max_length=120)
    slug =  models.SlugField(blank=True,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", null=True, blank=True )
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()
    
    # def get_absolute_url(self):
    #     # return "/products/{slug}/".format(slug=self.slug)
    #     return reverse("products:detail",kwargs={"slug":self.slug})

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=product)