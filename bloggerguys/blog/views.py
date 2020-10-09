from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import CommentForm


def homepage(request):
    # print(request.GET)   #Debugging
    blog_list = BlogPost.objects.order_by('id').all()
    paginator = Paginator(blog_list, 2)  # Show 2 contacts per page

    page = request.GET.get('page', 1)
    blogs = paginator.get_page(page)
    popular_posts = BlogPost.objects.order_by('?')[:5]

    context = {
        'blogs': blogs,
        'name': 'Explorer',
        'popular_posts': popular_posts,
        'comment_form': CommentForm()

    }

    return render(request, 'index.html', context)


def comment(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    form = CommentForm(request.POST)
    c = form.save(commit=False)
    c.blog = blog
    c.save()
    return redirect('/')
