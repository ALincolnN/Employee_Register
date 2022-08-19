from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('register',views.register, name='register'),
    path('<int:id>/',views.register, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('list',views.index, name='list'),
    



]