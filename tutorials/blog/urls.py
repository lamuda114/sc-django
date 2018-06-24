from django.urls import path
from . import views

app_name = 'blog'    #name 전달 하는 방법
urlpatterns = [
    path('', views.index, name='index'),
    path('<pk>/', views.post_detail, name='post_detail'),
    path('<int:post_pk>/comment/new/', views.comment_new, name='comment_new'),
]
