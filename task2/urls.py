from django.urls import path
import task2.views as views 

urlpatterns = [
    path('', views.index),
    path('action', views.action, name ='action'),
    path('created', views.create, name='create'),
    path('deleted', views.delete, name ='delete'),
    path('update', views.update, name ='update')
]