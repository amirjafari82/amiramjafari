from django.shortcuts import render, redirect
from django.views import View
from .forms import ProjectRequestForm
from .models import ProjectRequest as ProjectRequestModel
from django.contrib import messages

class ProjectRequest(View):
    form_class = ProjectRequestForm
    
    def get(self,req):
        return render(req,'projectreq/index.html',{'form':self.form_class})
    
    def post(self,req):
        form = self.form_class(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ProjectRequestModel.objects.create(fname=cd['fname'],lname=cd['lname'],title=cd['title'],desc=cd['desc'],phone=cd['phone']) # type: ignore
            messages.success(req,'درخواست شما با موفقیت ثبت شد.','success')
        return redirect('projectreq:projectreq')