from django import forms


class TweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "What's happening?",
                                                         'class': 'tweet_form', 'rows':3, 'cols':63}),
                            max_length=140, required=True, label=False)
