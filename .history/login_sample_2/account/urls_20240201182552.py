from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("calendar/", views.CalendarView.as_view(), name="calendar"),
    path("shop_list/", views.ShopListView.as_view(), name="shop_list"),
    path("search/", views.search_view, name="search"),
    path("get-event-data/<date>/", views.get_event_data, name="get_event_data"),
    path("add-event/", views.add_event, name="add_event"),
]
