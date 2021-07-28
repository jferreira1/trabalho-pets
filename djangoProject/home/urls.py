from django.urls import path
from django.contrib.auth import views as auth_views
from home import views as home_views

urlpatterns = [
    path('register/', home_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('home/', home_views.home_page, name='home-page'),
]