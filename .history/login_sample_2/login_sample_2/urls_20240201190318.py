from django.contrib import admin
from django.urls import path, include  # `include` をインポート
from account import views as account_views  # account アプリケーションのビューをインポート


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')), 
    path('', account_views.TopView.as_view(), name='root'),  
      # `account` アプリケーションの URL をインクルード
    # 必要に応じて他のアプリケーションの URL パターンをここに追加
]
