from django.contrib import admin
from .models import ProjectRequest

@admin.register(ProjectRequest)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title','phone','fname','lname','created')