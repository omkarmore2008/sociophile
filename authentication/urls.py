from django.urls import path
from . import views
urlpatterns = [
    path("", views.register_page, name='register'),
    path("login", views.login_user, name='login'),
    path("otp", views.otp_verification, name='otp'),
    path('logout', views.logout_user, name="logout")
]
