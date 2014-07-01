from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from blog.models import Article, Tag, Classification

# Create your views here.
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/index.html', context)
def detail(request, id):
    if request.method == 'GET':
        id = request.GET.get('id', '');
        blog = get_object_or_404(Article, pk = id)
    return render(request, 'blog/detail.html', {
        'blog': blog,
    })
