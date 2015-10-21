from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextFiel()
    slug = models.SlugField(max_length=200)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

