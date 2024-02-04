# from django.shortcuts import render

# # Create your views here.

# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import TemplateView

# from . import forms


# class TopView(TemplateView):
#     template_name = "account/top.html"

# class HomeView(TemplateView):
#     template_name = "account/home.html"

# class LoginView(LoginView):
#     """ログインページ"""
#     form_class = forms.LoginForm
#     template_name = "account/login.html"

# class LogoutView(LogoutView):
#     """ログアウトページ"""
#     template_name = "account/login.html"


# class SignUpView(TemplateView):   
#     """サインアップ""" 
#     template_name = "account/signup.html"

# from django.urls import reverse_lazy
# from django.views import generic
# from .forms import SignUpForm

# class SignUpView(generic.CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('account:login')
#     template_name = 'account/signup.html'

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.views.decorators.http import require_http_methods
from .models import Shop  # あなたのモデルに合わせて変更してください
from django.views.decorators.csrf import csrf_exempt
import json

class TopView(TemplateView):
    template_name = "account/top.html"

class HomeView(TemplateView):
    template_name = "account/home.html"

class LoginView(TemplateView):
    template_name = "account/login.html"

class LogoutView(TemplateView):
    template_name = "account/logout.html"

class SignUpView(TemplateView):
    template_name = "account/signup.html"

class CalendarView(TemplateView):
    template_name = "account/calendar.html"

class ShopListView(ListView):
    model = Shop
    template_name = "account/shop_list.html"

def search_view(request):
    # ここに検索機能のロジックを実装
    pass

@csrf_exempt
@require_http_methods(["POST"])
def add_event(request):
    # ここにイベント追加のロジックを実装
    data = json.loads(request.body)
    # イベントをデータベースに保存する処理をここに追加
    return JsonResponse({"status": "success"})

def get_event_data(request, date):
    # 指定された日付のイベントデータを取得するロジックを実装
    # 仮のレスポンスを返す
    events = []  # 実際にはデータベースからイベントを取得
    return JsonResponse(events, safe=False)
