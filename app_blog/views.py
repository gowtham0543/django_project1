from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm  # We'll create this form in the next step
from django.db.models import Q
from .forms import SearchForm

def post_add(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    return render(request, 'app_blog/post_add.html', {'form': form})

def post_list(request):
    form = SearchForm()
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'app_blog/post_list.html', {'form': form,'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'app_blog/post_details.html', {'post': post})

def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'app_blog/post_edit.html', {'form': form,'post':post})


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    
    return render(request, 'app_blog/post_delete.html', {'post': post})


#### == search ==


def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        else:
            results = []
    else:
        form = SearchForm()
        results = []

    return render(request, 'app_blog/post_search.html', {'form': form,'posts':results})
