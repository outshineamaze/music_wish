#coding: utf-8
from django.db import models
from django.shortcuts import redirect
import datetime
import markdown
from django.contrib  import admin



class Comments(models.Model):
    name = models.CharField(max_length = 20)
    contents = models.TextField(max_length=400)
    like = models.IntegerField()
    replays = models.IntegerField()
    updated=models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __unicode__(self):
        print '%s , %s, %s'%(self.name,self.contents,self.timestamp)


class Replay(Comments):
    replayobj= models.IntegerField()
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','contents','like','updated','timestamp')
class ReplayAdmin(admin.ModelAdmin):
    list_display=('name','contents','updated','timestamp')
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Replay,ReplayAdmin)