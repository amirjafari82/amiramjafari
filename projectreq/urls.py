from django.urls import path
from . import views

app_name = 'projectreq'
urlpatterns = [
    path('',views.ProjectRequest.as_view(),name='projectreq')
]