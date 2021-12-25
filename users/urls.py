from django.urls import path
from . import views
from curriculum.views import home

app_name = "users"

urlpatterns = [
    path('', home, name='home'  ),
    path('signin/', views.SigninUser, name='signin'),
    path('register/', views.RegisterUser, name='register'),
    path('logout/', views.LogoutUser, name='logout'),
]