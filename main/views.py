from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.db.models import Q
from django.contrib import messages

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
        like_articles=Article.objects.filter(
            Q(category=article.category) | Q(tags__in=article.tags.all())
        ).distinct().order_by('-created_at')[:6]

        context = {
            'article':article,
            'like_articles':like_articles,
        }
        return render(request,'detail-page.html',context)


class CommentCreateView(View):
    def post(self,request,slug):
        Comment.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            text=request.POST['text'],
            article=get_object_or_404(Article,slug=slug),
        )
        return redirect('article-details',slug=slug)


class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Debug (optional)
        print(name, email, phone, subject, message)

        messages.success(request, "Xabar yuborildi!")

        return redirect('contact-us')



def SearchArticlesView(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Article.objects.filter(
            Q(title__icontains=query) |
            Q(intro__icontains=query)
        )

    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })





