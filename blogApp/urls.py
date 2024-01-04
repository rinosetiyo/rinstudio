from django.urls import path
from blogApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single-post/<slug:slug>/', views.single_post, name='single_post'),
    path('category/', views.category, name='category'),
]