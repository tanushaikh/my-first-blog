from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.utils import timezone
# Create your views here.

def blog_list_view(request):
    posts =  Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html', {'posts':posts})


def blog_post_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        text = request.POST.get('text')
        post = Post(title=title, text=text, published_date=timezone.now())
        post.save()
        return redirect('blog_list')
    return render(request, 'blog/post_form.html', {'action': 'Create'})

# Edit post view
def post_edit_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.published_date = timezone.now()
        post.save()
        return redirect('blog_list')
    return render(request, 'blog/post_form.html', {'post': post, 'action': 'Edit'})