from django import forms

from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        max_tweet_length = 240
        content = self.cleaned_data.get('content')
        if len(content) > max_tweet_length:
            raise forms.ValidationError("This tweet is too long")
        return content
