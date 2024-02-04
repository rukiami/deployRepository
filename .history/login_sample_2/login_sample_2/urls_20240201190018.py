from django.contrib import admin
from django.urls import path, include  # `include` をインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),  # `account` アプリケーションの URL をインクルード
    path('http://yourdomain/account/')
    # 必要に応じて他のアプリケーションの URL パターンをここに追加
]
