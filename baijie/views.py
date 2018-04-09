# -*- coding: utf-8 -*-

import markdown
from .models import BaiJie, Movie
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


def aboutview(request):
    return render(request, 'baijie/about.html')


# 使用django 自带的装饰器函数，参数login_url= 将没有登录的用户转到自定义的登录界面
class MovieView(LoginRequiredMixin, ListView):
    # login_url 是绝对路径，即有斜杠的
    login_url = '/baijie/login/'
    redirect_field_name = 'next'
    model = Movie
    template_name = 'baijie/movie.html'
    context_object_name = "movie_list"
    paginate_by = 10


class MoviePlay(LoginRequiredMixin, DetailView):
    login_url = '/baijie/login/'
    redirect_field_name = 'next'
    model = Movie
    template_name = 'baijie/play.html'
    context_object_name = 'play'
    pk_url_kwarg = 'pk'


class HomeView(ListView):
    model = BaiJie
    template_name = 'baijie/home.html'
    context_object_name = 'baijies'
    paginate_by = 3


class BaijieDetailView(DetailView):
    model = BaiJie
    template_name = 'baijie/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get(self, request, *args, **kwargs):
        response = super(BaijieDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        obj = super(BaijieDetailView, self).get_object(queryset=None)
        # 有些扩展需要手动打开
        obj.body = markdown.markdown(obj.body, extensions=['markdown.extensions.extra', ])
        return obj
