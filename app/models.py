from django.db import models
import os
from django.db.models import Q
import random
from django.urls import reverse


class TutorialQuerySet(models.query.QuerySet):

    def search(self, query):
        lookup = (Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(tag__title__icontains=query)
            )

        return self.filter(lookup).distinct()

class TutorialManager(models.Manager):
    
    def get_queryset(self):
        return TutorialQuerySet(self.model,using=self.db)

    def search(self, query):
        return self.get_queryset().search(query)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class tutorial(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    objects = TutorialManager()

    def __str__(self):
        return self.title
