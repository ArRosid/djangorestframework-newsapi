from django.urls import path
from . import views

urlpatterns = [
    path('articles/',
        views.ArticleListCreateAPIVew.as_view(),
        name='article-list'),

    path('articles/<int:pk>/',
        views.ArticleDetailView.as_view(),
        name="article-detail"),
]