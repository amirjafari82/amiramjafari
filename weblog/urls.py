from django.urls import path
from . import views

app_name = 'weblog'
urlpatterns = [
    path('',views.WeblogHome.as_view(),name='weblog'),
    path('article/<int:pk>/',views.ArticleView.as_view(),name='article_detail'),
    path('article/co/<int:pk>/',views.PostPreLoadTaskView.as_view(),name='redirect_task')
]