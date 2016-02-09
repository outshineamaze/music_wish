# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from forms import CommentForm,ReplaycommentForm
from django.contrib import messages
from comments.models import Comments,Replay
from django.core.paginator import Paginator,InvalidPage, EmptyPage
from django.core import serializers
from django.template import Template, Context

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
        print page      # 如果没有对应的page键，就返回默认1
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


