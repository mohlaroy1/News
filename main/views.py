from django.shortcuts import render
from django.views import View

from .models import *


class HomeView(View):
    def get(self,request):
        top_articles=Article.pub_objects.order_by('-important', '-views')[:10]
        context = {'top_articles':top_articles}
        return render(request,'index.html', context)

    def post(self,request):
        pass
