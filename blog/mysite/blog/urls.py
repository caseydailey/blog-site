from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

# using generic list and detail views, we'll display the first five posts by date
urlpatterns = [url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:5], 
    template_name="blog/blog.html")),
# if you click on one of the posts, a detail view will display it's particulars
# the regex is just saying we expect one or more digits which django will recognize as the pk value ('blog/5' etc...)
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='blog/post.html'))]
