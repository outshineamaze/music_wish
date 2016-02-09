from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'comments.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^$', 'comments.views.errorpage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','comments.views.home',name="home"),
    url(r'^addcomments/','comments.views.addcomment',name='addcomment'),
    url(r'^addreplay/','comments.views.replaycom',name='addreplay')
)
