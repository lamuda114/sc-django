from django.urls import path
from . import views

app_name = 'blog'    #name 전달 하는 방법123
urlpatterns = [
    path('', views.index, name='index'),
    path('<pk>/', views.post_detail, name='post_detail'),
]
