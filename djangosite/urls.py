from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView as auth_views, LogoutView as lo
urlpatterns = [
    path('admin/', admin.site.urls),
    #agrego lo que esta aqui abajo
    path('', include('blog.urls')),

    path('accounts/login/', auth_views.as_view(), name=('login')),

    path('accounts/logout/', lo.as_view(), name=('logout'), kwargs={'next_page':'/'}),

    #path('accounts/logout', auth_views.as_view(), name='logout'),



]
