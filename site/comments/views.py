
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
# from forms import CommentForm,ReplaycommentForm
from django.contrib import messages
from comments.models import Comments,Replay,Song,Comment
from django.core.paginator import Paginator,InvalidPage, EmptyPage
from django.core import serializers
from django.template import Template, Context
from qiniu import Auth
from comments.api import NetEase
import re
def errorpage(request):
	return render(request,'comments/404page.html')

def home(request):
    print "start process"


    last_comment_list = Comments.objects.all().order_by("-timestamp")
    page_size=10
    paginator=Paginator(last_comment_list,page_size)
    print paginator.num_pages
    try:
        page=int(request.REQUEST.get('page',1))
  # 如果没有对应的page键，就返回默认1
    except ValueError:

        page = 1
        print page
    try:
        posts = paginator.page(page)
        print page
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    print "succcs"
    json_data = serializers.serialize("json", posts)
    contexts = {'commentList':posts}
    if page==1:
        return render(request,'comments/loadmore.html',contexts)
    else:
        t=Template('comments/ajax.html')
        html=t.render(Context(contexts))
        return HttpResponse(html)
def index(request):
    print "start process"


    last_comment_list = Comments.objects.all().order_by("-timestamp")
    page_size=10
    paginator=Paginator(last_comment_list,page_size)
    print paginator.num_pages
    try:
        page=int(request.REQUEST.get('page',1))
        print page      # 如果没有对应的page键，就返回默认1
    except ValueError:
        page = 1
        print page+"123242354353"
    try:
        posts = paginator.page(page)
        print page
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    print "succcs"
    context = {'commentList':posts}
    return render(request,'comments/index.html',context)



def addcomment(request):
    print "start process"
    if request.GET:
        name=request.GET['name']
        contents=request.GET['contents']
        like=request.GET['like']
        m=Comments(name=name,contents=contents,like=like,replays=0)
        m.save()
        print "success by get"
        return HttpResponse("success")

def replaycom(request):
    print "start process"
    if request.GET:
        name=request.GET['name']
        contents=request.GET['contents']
        replayobj=request.GET['replayobj']
        m=Replay(name=name,contents=contents,like=0,replays=0,replayobj=replayobj)
        m.save()
        print "success by gedfgst"
        print "hhhhhhhhhhhhhh"
        return HttpResponse("success")


def song(request,pk):
    song = Song.objects.get(id=pk)
    context = {"song":song}

    print song.id
    return  render(request,'comments/song.html',context)
def uploadsong(request):


    q = Auth('ToNLYIGLfHy5tpKSsRcBV2pw18b20LrYuBdvHaA_', 'rrD25c6RoHoMajmLR8lSz9wW4FcGEHvGMDL4l2zV')
    print q
    token = q.upload_token('outshineamazing', '')
    print token
    context = {'uptoken_url':token}
    return render(request,'comments/test.html',context)
def gettoken(request):
    q = Auth('ToNLYIGLfHy5tpKSsRcBV2pw18b20LrYuBdvHaA_', 'rrD25c6RoHoMajmLR8lSz9wW4FcGEHvGMDL4l2zV')
    print 'get a token request and return now'
    token = q.upload_token('outshineamazing', '')
    return HttpResponse('{ "uptoken": "'+token+'"}')
def addsong(request):
    link = request.GET['songlink']
    story=request.GET['contents']
    print link
    songid=re.split(r'id=', link)[1]
    # song_url ="http://link.hhtjim.com/163/"+ songid+".mp3"


    song=NetEase()
    a =song.song_detail(songid)
    print '---------------'
    name =a[0]['name']
    author = a[0]['artists']
    authorename= author[0]['name']
    song_pic= a[0]['album']['blurPicUrl']
    song_url= a[0]['mp3Url']
    print song_url
    song= Song(name=name,song_pic=song_pic,song_url=song_url,song_author=authorename,song_story=story)
    song.save()
    print 'song save success'
    return HttpResponse(song.id)








