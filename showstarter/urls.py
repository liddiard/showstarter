from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from analysis import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'showstarter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.FrontView.as_view(), name='front'),
    url(r'^show/(?P<show>\w+)/$', views.SingleShowView.as_view(), name='show'),

    url(r'^admin/', include(admin.site.urls)),
)
