from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweet_list_view, name='tweet_list'),
    path('create/', views.tweet_create_view, name='tweet_create'),
    path('<int:tweet_id>/', views.tweet_detail_view, name='tweet_detail'),
    path('<int:tweet_id>/delete/', views.tweet_delete_view, name='tweet_delete'),
    path('action/', views.tweet_action_view, name='tweet_action')
]
