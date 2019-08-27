from django.urls import path
from . import views

urlpatterns = [
    path('articles/',
        views.ArticleListCreateAPIVew.as_view(),
        name='article-list'),

    path('articles/<int:pk>/',
        views.ArticleDetailView.as_view(),
        name="article-detail"),

    path('journalists/',
        views.JournalistListCreateAPIView.as_view(),
        name='journalist-list'),

    path('journalists/<int:pk>/',
        views.JournalistDetaliAPIView.as_view(),
        name="journalist-detail"),

]