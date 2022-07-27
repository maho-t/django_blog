# users用URLパターンの定義

from django.urls import URLPattern, path, include

app_name = 'user'
urlpatterns = [
  path('', include('django.contrib.auth.urls')),
]