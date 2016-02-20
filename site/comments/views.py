
# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
# from forms import CommentForm,ReplaycommentForm
from django.contrib import messages
from comments.models import Comments,Replay,Song,Comment,SongInfo,SongList
from django.core.paginator import Paginator,InvalidPage, EmptyPage
from django.core import serializers
from django.template import Template, Context
from qiniu import Auth
from comments.api import NetEase, searchResult,songResult
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
    if SongList.objects.all():
        songlist=SongList.objects.all().order_by("-timestamp")[0]
        songids = songlist.songlist.split(",")
        songlistobj = SongInfo.objects.filter(id__in=songids)[0:10]
        context = {"resultlist":songlistobj}
        print "succcs"
        return render(request,'comments/search.html',context)
    else:
        return render(request,'comments/search.html',{})



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
    song_pic  = song.song_pic +"?param=130y130"
    context = {"song":song,'comments':posts,"song_pic":song_pic}
    if not isajax:
        print "return songhtml"
        return  render(request,'comments/song.html',context)
    elif isajax:
        print 'return ajax comment html'
        return render(request,'comments/ajax.html',context)
    else:
        return HttpResponse('error')




def addsong(request):
    try:
        songid = request.GET['songid']
        story_author= request.GET['username']
        story=request.GET['contents']

    except :
        return HttpResponse('error')
    try:
        song=NetEase()
        a =song.song_detail(songid)
    except :
        return HttpResponse('error')

    print '---------------'
    try:
        name =a[0]['name']
        author = a[0]['artists']
        authorename= author[0]['name']
        song_pic= a[0]['album']['blurPicUrl']
        song_url= a[0]['mp3Url']
        print song_url
    except:
        return HttpResponse("error")
    try:
        if not story_author:
            story_author="猜猜我是谁"
        if not story:
            story= "大爷我很深沉,啥都不想说"
        song= Song(name=name,song_pic=song_pic,song_url=song_url,song_author=authorename,song_story=story,story_author=story_author)
        song.save()
        print song.id
        return HttpResponse(song.id)
    except:
        return HttpResponse("error")


def search(request):
    try:
        if request.GET['keyword'] == "":
            #print request.GET['keyword']
            #print type(request.GET['keyword'])
            return HttpResponse('请输入要搜索的歌曲\(^o^)/~') 
        keyword =request.GET['keyword']
    except:
        return HttpResponse('输入有误重新输入\(^o^)/~')

    # seach= NetEase()
    # res = seach.search(keyword)
    # print type(res)
    # # print res['result']['songs']
    # songlist = [[a['id'], a['name'], a['artists'][0]['name']]for a in res['result']['songs']]
    try:
        if re.findall(r'/song/(\d+)', keyword):
            songid=re.findall(r'/song/(\d+)', keyword)
            print songid[0]
            songlist=searchResult.getSongResult(songid[0])
        else:
            songlist=searchResult.getSearchResult(keyword)
        contents = {"resultlist":songlist}
        return render(request,"comments/searchlist.html",contents)
    except:
        return HttpResponse('服务器晚上要挨打了')

def genSongList(request):
    try:
        if request.GET['keyword'] == "":
            print request.GET['keyword']
            print type(request.GET['keyword'])
            return HttpResponse('请输入要搜索的歌单\(^o^)/~') 
        keyword =request.GET['keyword']
        name = request.GET.get("name","不好听你来打我啊")
        author = request.GET.get("author","梦很想家")
    except:
        return HttpResponse('输入有误重新输入\(^o^)/~')
    print keyword
    if re.findall(r'id=(\d+)', keyword):
        listid = re.findall(r'id=(\d+)', keyword)[0]
        print listid
        songlist = songResult.getSongList(listid)
        songlist_str=",".join([str(item.id) for item in songlist])
        SongList(name=name,author= author,songlist=songlist_str).save()
        print songlist_str
        for item in songlist:
            if SongInfo.objects.filter(id=int(item.id)):
                print "find simer song"
            else:
                SongInfo(id=int(item.id),name=item.name,author=item.author,mp3url=item.mp3url,albumpicurl=item.albumpicurl).save()
                print "success insert a song"

        return HttpResponse("success")
    else:
        return HttpResponse("妈的智障,找不到啊")

def dailysonglist(request):
    return render(request,"comments/dailysonglist.html",{})

def newcomment(request):
    print "start process"
    if request.GET:
        print 'get'
        if request.GET.get('parent_comment',None)!=None:
            songid= request.GET['parentid']
            name=request.GET['name']
            contents=request.GET['contents']
            replayobj=request.GET['parent_comment']
            # print 'replay'
            # print songid
            # print 'name:'+name
            # print 'comments:'+contents

            if len(name)<1 or len(contents)<5:
                return HttpResponse('error1')
            elif len(name)>50 or len(contents)>400:
                return HttpResponse("error2")
            m=Comment(parent_song_id=songid,name=name,contents=contents,parent_comment=replayobj)
            m.save()
            print "success add replay commment "
            return HttpResponse("success")
        else:
            songid= request.GET['parentid']
            name=request.GET['name']
            contents=request.GET['contents']
            # print songid
            # print 'name:'+name
            # print 'comments:'+contents

            if len(name)<1 or len(contents)<5:
                return HttpResponse('error1')
            elif len(name)>50 or len(contents)>400:
                return HttpResponse("error2")
            m=Comment(parent_song_id=songid,name=name,contents=contents)
            m.save()
            print "success by direct add comment "
            return HttpResponse("success")
    else:
        return HttpResponse('error0')

    

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
        return HttpResponse("success")