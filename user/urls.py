# users用URLパターンの定義

from django.urls import URLPattern, path, include

from . import views

app_name = 'user'
urlpatterns = [
  # デフォルトの認証URLを読み込む
  path('', include('django.contrib.auth.urls')),
  # ユーザー登録ページ
  path('register/', views.register, name='register'),
]