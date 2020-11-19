from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('tweets/<int:tweet_id>/', views.tweet_detail_view, name='tweet_detail')
]
