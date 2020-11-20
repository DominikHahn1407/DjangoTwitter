from django.conf import  settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url

from .models import Tweet
from .forms import TweetForm


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request):
    return render(request, 'tweets/home.html', context={}, status=200)


def tweet_create_view(request):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse({}, status=201) # 201 == created Items
        if next_url is not None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})


# Rest API View for JavaScript Consumption
def tweet_list_view(request):
    tweets = Tweet.objects.all()
    tweets_list = [tweet.serialize() for tweet in tweets]
    data = {
        "isUser": False,
        "response": tweets_list
    }

    return JsonResponse(data)


# Rest API View for JavaScript Consumption
def tweet_detail_view(request, tweet_id):
    data = {
        "id": tweet_id
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not found'
        status = 404

    return JsonResponse(data, status=status)
