from django.db import models
from django_jalali.db import models as jmodels

class Weblog(models.Model):
    image = models.ImageField(upload_to='static/images/weblog')
    title = models.CharField(max_length=80,default=None)
    slug = models.SlugField(allow_unicode=True)
    body = models.TextField(default=None)
    view = models.IntegerField(default=0)
    created = jmodels.jDateTimeField(auto_now_add=True)