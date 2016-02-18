#coding: utf-8

from django.db import models
from django.shortcuts import redirect
import datetime
import markdown
from django.contrib  import admin



class Song(models.Model):
    name = models.CharField(max_length = 20)
    song_pic= models.CharField(max_length=200,null=True,blank=True)
    song_url= models.CharField(max_length=200)
    song_author = models.CharField(max_length=50,null=True,blank=True)
    song_des =models.TextField(max_length=400,null=True,blank=True)
    song_story = models.TextField(max_length=1000)
    story_author = models.CharField(max_length=50,null=True,blank=True)
    like = models.IntegerField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'歌曲'
        verbose_name_plural = u'歌曲_管理'


class Comment(models.Model):
    parent_song=models.ForeignKey(Song)
    name = models.CharField(max_length = 20)
    contents = models.TextField(max_length=400)
    like = models.IntegerField(null=True,blank=True)
    replays = models.IntegerField(default=0)
    parent_comment= models.IntegerField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __unicode__(self):
        return str(self.id)
    def __str__(self):
        return self.id
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论_管理'

class Comments(models.Model):
    name = models.CharField(max_length = 20)
    contents = models.TextField(max_length=400)
    like = models.IntegerField()
    replays = models.IntegerField()
    updated=models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __unicode__(self):
        print '%s , %s, %s'%(self.name,self.contents,self.timestamp)

class  SongAdmin(admin.ModelAdmin):
    list_display = ('name','song_pic','song_url','song_story','updated')
        
class Replay(Comments):
    replayobj= models.IntegerField()

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','contents','updated','timestamp')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','contents','updated','timestamp')
class ReplayAdmin(admin.ModelAdmin):
    list_display=('name','contents','updated','timestamp')

admin.site.register(Comments,CommentsAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Replay,ReplayAdmin)
admin.site.register(Song,SongAdmin)