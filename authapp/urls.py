
from django.urls import path
from .import views 

urlpatterns = [

    # path('', views.base,name='base'),
    path('', views.home,name='home'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]