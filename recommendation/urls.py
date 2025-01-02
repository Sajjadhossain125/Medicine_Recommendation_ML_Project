from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
