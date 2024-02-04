from django.contrib import admin
from django.urls import path, include  # include をインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),  # account アプリケーションの urls.py をインクルード
    # 他のアプリケーションのルーティングもここに追加
]