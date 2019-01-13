from django.urls import path
from . import views

app_name = "yb123"

urlpatterns = [
    path('', views.index, name='one'),
    path('two/', views.tow, name='two'),
    path('three/', views.three, name='three'),
]