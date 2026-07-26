from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def index(request):
    objs = Article.objects.all()
    context = {
        "articles": objs,
    }
    
    return render(request, "blog/blogs.html", context=context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    print(obj)
    context = {
        "article": obj,
    }
    
    return render(request, "blog/article.html", context=context)