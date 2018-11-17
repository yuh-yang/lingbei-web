from django.shortcuts import render
from website.models import save_tweets
from django.contrib.auth.models import User  # User models

# 没有写完的部分最好在不影响运行的情况下pass掉 以便调试

def make_tweet(request):
    """请写一下函数大概的设计思路、放置位置和安排"""
    pass
    username =  # 获取用户名 使用GET方法？
    date = request.GET.get('date')
    time = request.GET.get('time')
    place = request.GET.get('place')
    thing = request.GET.get('thing')
    save_tweets(username, date, time, place, thing)
    return  # 提示发布成功

def user_login(request):
    pass
    """
    思路: 
        第一次登陆时自动注册 并实现自动跳转
        之后登陆依靠cookie记录（自动保存密码吧）
        但是这样就要查询数据库中是否存在此字段……
    """
    userID = request. # <string>, 实现方法待定
    userPW = request. # <string>, ...
    getUser = User.object.filter(username=userID)
    if (getUser.exists() == 0):
        # 不存在该用户 注册
        User.objects.create_user(username=userID, password=userPW)
    elif (getUser.password != userPW):
        # 密码错误！
        # 要求重新输入
    
    # 登陆模块
    
    return # 提示注册成功

