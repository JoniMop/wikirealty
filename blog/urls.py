from django.urls import path
from . import views
from django.contrib.auth.views import LoginView as auth_views
urlpatterns = [
    #localhost:8000
    path('', views.post_list, name='post_list'),
    #
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #localhost/post/new   
    path('post/new/', views.post_new, name='post_new'),
    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('signup/', views.signup, name='signup'),

]