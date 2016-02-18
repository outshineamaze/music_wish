
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
from comments.api import NetEase, searchResult
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
    print "succcs"
    context = {}
    return render(request,'comments/search.html',context)



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

def song(request,pk):
    song = Song.objects.get(id=pk)
    comments = Comment.objects.filter(parent_song=pk).order_by('-timestamp')

    page_size=5
    paginator=Paginator(comments,page_size)
    print paginator.num_pages
    isajax = False
    try:
        if request.GET.get('page',None)!= None:
            page=int(request.GET.get('page',1))
            print page
            isajax = True
        else:
            page=1
    except ValueError:
        return HttpResponse('error')
    try:
        posts = paginator.page(page)
        print page
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    print "succcs  get post object "
    context = {"song":song,'comments':posts}
    if not isajax:
        print "return songhtml"
        return  render(request,'comments/song.html',context)
    elif isajax:
        print 'return ajax comment html'
        return render(request,'comments/ajax.html',context)
    else:
        return HttpResponse('error')




def addsong(request):
    link = request.GET['songlink']
    story=request.GET['contents']
    print link
    songid=re.split(r'id=', link)[1]
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
    print song.id
    return HttpResponse(song.id)


def search(request):
    try:
        keyword =request.GET['keyword']
        if not request.GET['keyword']:
            return HttpResponse('请输入要搜索的歌曲\(^o^)/~') 
    except:
        return HttpResponse('error')

    # seach= NetEase()
    # res = seach.search(keyword)
    # print type(res)
    # # print res['result']['songs']
    # songlist = [[a['id'], a['name'], a['artists'][0]['name']]for a in res['result']['songs']]
    songlist=searchResult.getSearchResult(keyword)
    contents = {"resultlist":songlist}
    return render(request,"comments/searchlist.html",contents)


def newcomment(request):
    print "start process"
    if request.GET:
        print 'get'
        if request.GET.get('parent_comment',None)!=None:
            songid= request.GET['parentid']
            name=request.GET['name']
            contents=request.GET['contents']
            replayobj=request.GET['parent_comment']
            print 'replay'
            print songid
            print 'name:'+name
            print 'comments:'+contents

            if name=='' or contents=='':
                return HttpResponse('null')
            m=Comment(parent_song_id=songid,name=name,contents=contents,parent_comment=replayobj)
            m.save()
            print "success "
            return HttpResponse("success")
        else:
            songid= request.GET['parentid']
            name=request.GET['name']
            contents=request.GET['contents']
            print songid
            print 'name:'+name
            print 'comments:'+contents

            if name=='' or contents=='':
                return HttpResponse('null')
            m=Comment(parent_song_id=songid,name=name,contents=contents)
            m.save()
            print "success by direct add comment "
            return HttpResponse("success")
    else:
        return HttpResponse('error')

    

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