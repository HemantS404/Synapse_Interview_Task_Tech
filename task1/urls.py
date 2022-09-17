from django.urls import path
import task1.views as views

urlpatterns = [
    path('', views.index),
    path('Sub_breed', views.s_r, name='sub'),
]