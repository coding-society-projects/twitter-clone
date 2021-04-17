from django.contrib import admin

from tweet.models import Tweet, UserProfile

admin.site.register(Tweet)
admin.site.register(UserProfile)
