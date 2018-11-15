from django.shortcuts import render
from website.models import save_tweets

def make_tweet(request):
    username =  #获取用户名
    date = request.GET.get('date')
    time = request.GET.get('time')
    place = request.GET.get('place')
    thing = request.GET.get('thing')
    save_tweets(username, date, time, place, thing)
    return #提示发布成功
# Create your views here.
