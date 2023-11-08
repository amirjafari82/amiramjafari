from django.db import models

class Resume(models.Model):
    image = models.ImageField(upload_to='static/images/resume')
    webname = models.CharField(max_length=80)
    link = models.URLField(max_length=100)