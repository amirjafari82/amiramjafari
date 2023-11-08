from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
from .models import Resume as ResumeModel

class Resume(View):
    
    def get(self,req):
        resumes = ResumeModel.objects.all()
        return render(req,'resume/index.html',{'resumes':resumes})