from django.shortcuts import render

from tweet.models import Tweet


def feed(request):
    tweets = Tweet.objects.order_by('-post_date')
    context = {'tweets': tweets}
    return render(request, "tweet/feed.html", context)
