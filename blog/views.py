from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q


class TagTV(TemplateView) :
    template_name = "tagging/tagging_cloud.html"


class PostTOL(TaggedObjectList) :
    model = Post
    template_name = 'tagging/tagging_post_list.html'


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
    month_format = '%m'


class PostDAV(DayArchiveView) :
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView) :
    model = Post
    date_field = 'modify_date'


class SearchFormView(FormView) :
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)