from django.urls import path

from .views import TopView, HomeView, LoginView, LogoutView


app_name="account"
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]  

from .views import SignUpView

urlpatterns = [
    # ...既存のURLパターン...
    path('signup/', SignUpView.as_view(), name='signup'),
]

from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', views.TopView.as_view(), name='top'),  # トップページへのパスを追加
    # ...他のURLパターン...
]
