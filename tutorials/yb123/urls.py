from django.urls import path
from . import views

app_name = "yb123"

urlpatterns = [
    path('', views.index, name='one'),
    path('tow/', views.tow, name='tow'),
    path('three/', views.three, name='three'),
]