from django.shortcuts import render

from apps.elen.models import Blog

from django.core.paginator import Paginator


def home(request):
    cat = request.GET.get('cat')

    blogs = Blog.objects.all().order_by('?')[:12]

    if cat:
        blogs = blogs.filter(category__name=cat)

    context = {
        'blogs': blogs,
    }

    return render(request, 'index.html', context)

def photography(request):
    cat = request.GET.get('cat')

    blogs = Blog.objects.filter(category__name="Photography").order_by('?')[:12]

    context = {
        'blogs': blogs,
        }
    
    return render(request, 'photography.html', context)

def travel(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    page_number = request.GET.get('page')

    blogs = Blog.objects.filter(category__name="Travel").order_by('?')
    popular_blogs = Blog.objects.all().order_by('-id')[:3]

    paginator = Paginator(blogs, 5)
    selected_page = paginator.get_page(page_number)
    selected_page.adjusted_elided_pages = paginator.get_elided_page_range(page_number)

    context = {
        'blogs': selected_page,
        'popular_blogs': popular_blogs,
    }

    return render(request, 'travel.html', context)

def fashion(request):
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')

    blogs = Blog.objects.filter(category__name="Fashion").order_by('?')[:12]
    popular_blogs = Blog.objects.all().order_by('-id')[:3]

    context = {
        'blogs': blogs,
        'popular_blogs': popular_blogs,
    }

    return render(request, 'fashion.html', context)
