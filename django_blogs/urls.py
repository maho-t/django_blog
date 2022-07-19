# django_blogsのURLパターンの定義
from django.urls import path
from . import views

app_name = 'django_blogs'
urlpatterns = [
    #ホームページ
    path('', views.index, name='index'),
    # すべてのトピックを表示するページ
    path('topics/', views.topics, name='topics'),
    # 個別トピックの詳細ページ
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
