
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('navigator/', views.navigator, name="navigator"),
    path('signup/', views.handleSignup, name='signup'),
    path('login-landing/', views.handleLogin, name='login'),
    path('logout-user/', views.handleLogout, name='logout'),
    path('adminCorner/', views.admin_page, name='admin')
]
