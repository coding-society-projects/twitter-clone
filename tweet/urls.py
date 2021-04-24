from django.urls import path
from . import views

urlpatterns = [
    path('tweet/feed', views.feed),
    path('tweet/search', views.search),
    path('profile/<str:username>', views.profile),
    path('tweet/delete/<int:id>', views.delete_tweet),
    path('', views.index),
]