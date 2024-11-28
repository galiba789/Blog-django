from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForms

def frontpage(request):
    posts = Post.objects.all()

    
    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForms(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForms()
    
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})
