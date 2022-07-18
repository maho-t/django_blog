# django_blogsのURLパターンの定義
from django.urls import path
from . import views

app_name = 'django_blogs'
urlpatterns = [
    #ホームページ
    path('', views.index, name='index'),
]
