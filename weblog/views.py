from typing import Any, Dict, Optional
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
from .models import Weblog
from django.db.models import F
from jdatetime import datetime

class WeblogHome(View):
    
    def get(self,req):
        articles = Weblog.objects.all()
        return render(req,'weblog/index.html',{'articles':articles})
    
class ArticleView(View):
    
    def get(self,req,pk):
        article = get_object_or_404(Weblog,id=pk)
        return render(req,'weblog/article.html',{'article':article})
    
class PostPreLoadTaskView(RedirectView):
    pattern_name = 'weblog:article_detail'
    
    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Weblog, pk=kwargs['pk'])
        article.view = F('view') + 1
        article.save()
        return super().get_redirect_url(*args, **kwargs)
    