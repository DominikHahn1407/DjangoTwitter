from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Tweet


def home_view(request):
    return render(request, 'base.html')


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
