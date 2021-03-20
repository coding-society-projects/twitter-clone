from django import forms


class TweetForm(forms.Form):
    tweet = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "What's happening?", 'rows':4, 'cols':45}),
                            max_length=140, required=True, label=False)
