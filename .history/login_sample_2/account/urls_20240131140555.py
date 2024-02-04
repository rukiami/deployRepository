from django.urls import path
from .views import (
    TopView, HomeView, LoginView, LogoutView, SignUpView,
    CalendarView, ShopListView, search_view, get_event_data, add_event, get_events # get_event_data をインポートする
)

app_name="account"

urlpatterns = [
    path("", TopView.as_view(), name="top"),
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('shop_list/', ShopListView.as_view(), name='shop_list'),
    path('search/', search_view, name='search'),  # search の URL パターンを追加
    path('get-event-data/<date>/', get_event_data, name='get_event_data'),
    path('add-event/', add_event, name='add_event'),
    path('get-events/', get_events, name='get_events'),
    
    # ...他にも必要なURLパターンがあれば追加...
]  

