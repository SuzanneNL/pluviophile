from django.shortcuts import render


def blog_posts_list(request):
    return render(request, 'blog/blog_posts_list.html', {})
