from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('',views.Resume.as_view(),name='resume'),
]