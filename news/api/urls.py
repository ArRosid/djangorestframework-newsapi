from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list_create_api_view, name='article-list'),
    path('articles/<int:pk>/', views.article_detail_api_view, name="article-detail"),
]