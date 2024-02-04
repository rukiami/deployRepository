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
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import LoginForm, SignUpForm
from .models import Shop, Event  # Event モデルをインポートする
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import json
from django.utils.dateparse import parse_date


class TopView(TemplateView):
    template_name = "account/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "account/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = "account/login.html"

class LogoutView(LogoutView):
    """ログアウトページ"""
    template_name = "account/login.html"

class SignUpView(CreateView):
    """サインアップ"""
    form_class = SignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'

class CalendarView(TemplateView):
    template_name = 'account/calendar.html'  # calendar.html テンプレートを使用する

class ShopListView(ListView):
    model = Shop
    template_name = 'account/shop_list.html'   

def search_view(request):
    query = request.GET.get('q', '')
    if query:
        results = Shop.objects.filter(name__icontains=query)  # 'name' は Shop モデルの属性
    else:
        results = []

    context = {
        'query': query,
        'results': results
    }
    # 検索機能の実装をここに書きます
    # この例では単純に search.html テンプレートをレンダリングします
    return render(request, 'account/search.html', context)


# views.py

# ...他のimport文...

# class CalendarView(LoginRequiredMixin, TemplateView):
#     template_name = 'account/calendar.html'

# ...他のビュークラス...

# from django.views.generic import TemplateView, ListView
# from django.http import JsonResponse
# from .models import Event
# import json
# import logging
# from django.utils.dateparse import parse_date
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_http_methods
# from django.core.serializers import serialize
# ...他のビュークラス...



class CalendarView(TemplateView):
    template_name = 'account/calendar.html'  # calendar.html テンプレートを使用する

# ...他のビュークラス...
    
class ShopListView(ListView):
    model = Shop
    template_name = 'account/shop_list.html'

def get_event_data(request, date_str):
    # date_strに基づいてイベントデータをフィルタリング
    events = Event.objects.filter(date=date_str)
    # イベントデータをシリアライズしてJSONで返す
    data = serialize('json', events)
    return JsonResponse(data, safe=False)

# ここに get_events 関数を追加
def get_events(request):
    # イベントのリストを取得して返すロジック
    events = Event.objects.all()
    data = serialize('json', events, fields=('title', 'date'))
    return JsonResponse(data, safe=False)    

# from django.http import JsonResponse
# from .models import Event

# import logging
# from django.views.decorators.http import require_http_methods
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .models import Event



# from .models import Event  # Eventモデルがあると仮定しています
# ロガーの設定
# logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["POST"])
def add_event(request):
    try:
        data = json.loads(request.body)
        event = Event.objects.create(
            title=data['title'],
            date=parse_date(data['date']),
            # 必要に応じて他のフィールドも追加
        )
        return JsonResponse({'status': 'success', 'event_id': event.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # except Exception as e:
    #     return JsonResponse({'status': 'error', 'error': str(e)}, status=400)
        
        # Eventモデルのdateフィールドがdatetime.dateを期待している場合のみ必要
        # if not event_date:
        #     raise ValueError('Invalid date format')

        