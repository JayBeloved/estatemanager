from django.urls import path,include
from django.contrib.auth.views import LogoutView as logout_view
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),

    path('profile/', views.user_profile, name="profile"),

    path('logout/', logout_view.as_view(), name="logout"),
]