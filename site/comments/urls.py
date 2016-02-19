from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comments.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','comments.views.home',name="home"),

     url(r'^uploadsong/$','comments.views.uploadsong',name="loadsong"),
     url(r'^uploadsong/gettoken','comments.views.gettoken',name="gettoken"),
    url(r'^song/(?P<pk>\d+)/','comments.views.song',name="song"),

   

    url(r'^addsong/','comments.views.addsong',name='addsong'),
    url(r'^gensonglist/','comments.views.genSongList',name="gensonglist"),
    url(r'^search/','comments.views.search',name='search'),
    url(r'^newcomment/','comments.views.newcomment',name='newcomment'),

    #older functions
 	url(r'^addcomments/','comments.views.addcomment',name='addcomment'),
    url(r'^addreplay/','comments.views.replaycom',name='addreplay'),

)
