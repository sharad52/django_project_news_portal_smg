from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import News

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'recent_news'

    def get_queryset(self):
        return News.objects.order_by('-created_at')[:5]
# def index(request):
#     recent = News.objects.order_by('-created_at')

#     context = {'recent_news':recent,}
#     return render(request,'pages/index.html',context)

def detail(request,news_id):
    full_news = get_object_or_404(News,pk=news_id)
    context = {
        'full_news':full_news

    }
    return render(request,'pages/seeMore.html',context)

def factorial(request):
    n = int(request.GET["num1"])
    def factorialFunc(n): 
        if n == 0:
            return 1
        return n*factorialFunc(n-1)

    z = factorialFunc(n)
    return render(request,"testhtml/test.html",{'calValue':z,'givValue':n})
