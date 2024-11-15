
from django.urls import path

from . import views 



urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('get_user/', views.get_user, name='get_user'),
    path('login/', views.login_user, name='login_user'),
    path('update/', views.update_user, name='update_user'),
    path('delete/', views.delete_user, name='delete_user'),
]
