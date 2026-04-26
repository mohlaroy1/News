from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import DetailView

from .models import *


class HomeView(View):
    def get(self,request):
        top_articles=Article.pub_objects.order_by('-important', '-views')[:10]
        latest_news=Article.pub_objects.order_by('-created_at')[:8]
        most_viewed=Article.pub_objects.order_by('-views')[1:11]
        context = {'top_articles':top_articles,
                   'latest_news':latest_news,
                   'most_viewed':most_viewed,
        }
        return render(request,'index.html', context)


class NewsletterCreateView(View):
    def post(self,request):
        Newsletter.objects.create(
            email=request.POST['email'],
        )
        return redirect('home')


class ArticleDetailsView(DetailView):
    def get(self,request,slug):
        article=get_object_or_404(Article,slug=slug)
        context = {'article':article}
        return render(request,'detail-page.html',context)








