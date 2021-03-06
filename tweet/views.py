from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from tweet.models import Tweet


def index(request):
    return render(request, "tweet/index.html")

def feed(request):
    tweets = Tweet.objects.order_by('-post_date')
    context = {'tweets': tweets}
    return render(request, "tweet/feed.html", context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    id = user.id
    tweets = Tweet.objects.filter(user = id)
    context = {
        "tweets": tweets,
        "username": username,
    }
    return render(request, 'tweet/profile.html', context)
