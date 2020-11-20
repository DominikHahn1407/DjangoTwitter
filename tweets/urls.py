from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('tweets/', views.tweet_list_view, name='tweet_list'),
    path('tweets/create/', views.tweet_create_view, name='tweet_create'),
    path('tweets/<int:tweet_id>/', views.tweet_detail_view, name='tweet_detail')
]
