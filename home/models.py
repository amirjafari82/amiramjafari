from django.db import models
from django.core.exceptions import ValidationError
from django_jalali.db import models as jmodels 
    

class Contact(models.Model):
    name = models.CharField(max_length=35)
    phone = models.CharField(max_length=11)
    title = models.CharField(max_length=50)
    message = models.TextField()
    created = jmodels.jDateTimeField(auto_now_add=True)
    answered = models.BooleanField(default=False)