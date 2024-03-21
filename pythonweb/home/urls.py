from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Trang chủ
    path('contact/', views.contact, name='contact'),  # Trang liên hệ
    path('register/', views.register, name='register'),  # Trang đăng ký
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),  # Trang đăng nhập
    path('logout/', views.logout, name='logout'),  # Đường dẫn để logout
]
