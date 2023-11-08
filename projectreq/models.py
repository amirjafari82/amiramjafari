from django.db import models
from django_jalali.db import models as jmodels

class ProjectRequest(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    phone = models.CharField(max_length=11)
    created = jmodels.jDateTimeField(auto_now_add=True)