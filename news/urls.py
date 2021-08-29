from django.urls import path
from news.views import index, preview
from . import views

app_name = 'news'

urlpatterns = [
    path('', index, name = 'news-index'),
    path('news/preview/<int:id>', preview, name = 'news-preview'),

    path('api/get-news', views.NewsAPI.as_view()),
]
