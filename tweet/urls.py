from django.urls import path
from . import views

urlpatterns = [
    path('tweet/feed', views.feed),
    path('profile/<str:username>', views.profile),
    path('', views.index),
]