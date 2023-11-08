from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title','name','phone','answered','created')