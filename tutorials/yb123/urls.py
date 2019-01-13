from django.urls import path
from . import views

app_name = "yb123"

urlpatterns = [
    path('one/', views.one, name='one'),
    path('two/', views.two, name='two'),
    path('three/', views.three, name='three'),
]