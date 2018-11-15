from django.db import models

# Create your models here.
class UserInfo (models.Model):
    username = models.TextField()
    password = models.TextField()

    def __unicode__(self):
        return self.username

class Tweet(models.Model):
    username = models.TextField()
    date = models.DateField()
    time = models.TextField()
    place = models.TextField()
    thing = models.TextField()

    def __unicode__(self):
        return self.username, self.date, self.time, self.place

def save_tweets(un,dt,tm,pl,th): #存储一条发布
    Tweet.objects.create(username=un, date=dt, time=tm, place=pl, thing=th)

def contrast(user1, user2): #比较相似性
    #
