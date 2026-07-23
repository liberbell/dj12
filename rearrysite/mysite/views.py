from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def index(request):
    context = {
        "title": "Really origin site"
    }
    return render(request, "mysite/index.html", context)