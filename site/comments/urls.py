from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comments.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^$', 'comments.views.errorpage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','comments.views.home',name="home"),
     url(r'^uploadsong/$','comments.views.uploadsong',name="loadsong"),
     url(r'^uploadsong/gettoken','comments.views.gettoken',name="gettoken"),
    url(r'^song/(?P<pk>\d+)/','comments.views.song',name="song"),

    url(r'^addcomments/','comments.views.addcomment',name='addcomment'),
    url(r'^addreplay/','comments.views.replaycom',name='addreplay'),
    url(r'^addsong/','comments.views.addsong',name='addsong')
)
