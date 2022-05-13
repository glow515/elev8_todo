#urls file for todo app
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('sign',views.sign,name='sign'),
    path('edit',views.edit,name='edit'),
    path('log',views.log,name='log'),
    path('profile',views.profile,name='profile'),
    path('add_task',views.add_task,name='add_task'),
]
