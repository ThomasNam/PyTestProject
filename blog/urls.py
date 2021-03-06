from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),

    url(r'^post/$', PostLV.as_view(), name='post_list'),

    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),

    # /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),

    # /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[0-9]+)/$', PostMAV.as_view(), name='post_month_archive'),

    # /2012/nov/10
    url(r'^(?P<year>\d{4})/(?P<month>[0-9]+)/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),

    # /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),

    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),

    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    url(r'^search/$', SearchFormView.as_view(), name='search'),

    url(r'^add/$', PostCreateView.as_view(), name='add'),

    url(r'^change/$', PostChangeLV.as_view(), name='change'),

    url(r'^(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='update'),

    url(r'^(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='delete'),


]
