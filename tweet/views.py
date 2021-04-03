from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from tweet.forms import TweetForm
from tweet.models import Tweet


def index(request):
    return render(request, "tweet/index.html")


@login_required
def feed(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = Tweet()
            tweet.content = form.cleaned_data['tweet']
            tweet.image = form.cleaned_data.get('image')
            tweet.user = request.user
            tweet.save()
            form = TweetForm()
    else:
        form = TweetForm()
    tweets = Tweet.objects.order_by('-post_date')
    context = {
        'tweets': tweets,
        'form': form,
        'user': request.user,
    }
    return render(request, "tweet/feed.html", context)


@login_required
def profile(request, username):
    tweets = []
    error = ""
    try:
        user = User.objects.get(username=username)
        id = user.id
        tweets = Tweet.objects.filter(user=id)
    except ObjectDoesNotExist:
        error = "User does not exist"
    context = {
        "tweets": tweets,
        "username": username,
        "error": error,
    }
    return render(request, 'tweet/profile.html', context)
