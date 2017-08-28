from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post


# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'

    # 컨텍스트 변수명을 수정한다
    content_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView) :
    model = Post


class PostAV(ArchiveIndexView) :
    model = Post
    # 기준이 되는 날짜 필드
    date_field = 'modify_date'


class PostYAV(YearArchiveView) :
    model = Post
    date_field = 'modify_date'

    # 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿을 넘겨줌
    make_object_list = True


class PostMAV(MonthArchiveView) :
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView) :
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView) :
    model = Post
    date_field = 'modify_date'


