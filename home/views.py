from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from weblog.models import Weblog
from .forms import ContactForm

class Home(View):
    form_class = ContactForm
    
    def get(self,req):
        articles = Weblog.objects.all()
        return render(req, 'home/index.html',{'articles':articles,'form':self.form_class})
    
    def post(self,req):
        form = self.form_class(req.POST)
        form.save()
        messages.success(req,'پیام شما با موفقیت ارسال شد','success')
        return redirect('home:home')

class AboutMe(View):
    
    def get(self,req):
        return render(req,'home/aboutme.html')