from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist

from tweet.forms import TweetForm
from tweet.models import Tweet, UserProfile


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


def search(request):
    search_text = request.GET.get('search-text')
    context = {'tweets': Tweet.objects.filter(content__contains=search_text),
               'search_text': search_text,
               }
    return render(request, 'tweet/search.html', context)


def delete_tweet(request, id):
    tweet = Tweet.objects.filter(id=id).first()
    user = request.user
    if tweet.user == user:
        tweet.delete()

    return redirect('/tweet/feed')

