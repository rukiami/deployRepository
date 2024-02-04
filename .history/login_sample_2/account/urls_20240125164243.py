from django.urls import path

from .import views

app_name="account"
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]  

# account/urls.py
from django.urls import path
from . views import TopView, CalendarView, LoginView, SignUpView, HomeView
  # CalendarViewをimport

app_name = 'account'  # アプリケーションの名前空間を設定

urlpatterns = [
    # 他のURLパターン
    path('', TopView.as_view(), name='top'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('login/', LoginView.as_view(), name='login'),  # ログインページ
    path('signup/', SignUpView.as_view(), name='signup'),  # サインアップページ
    path('home/', HomeView.as_view(), name='home'),  # ホームページ
    # ...他にも必要なURLパターンがあればここに追加...
]
