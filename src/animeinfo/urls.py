from django.urls import path, include
from . import views

app_name = 'anime'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/<str:slug>/', views.info, name='info')
]
