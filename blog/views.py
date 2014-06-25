from django.shortcuts import render 
from django.template import RequestContext
from blog.models import Article, Tag, Classification

# Create your views here.
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/index.html', context)
