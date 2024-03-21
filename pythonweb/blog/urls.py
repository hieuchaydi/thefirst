from django.urls import path
from .views import PostListView, PostDetailView
from .models import Post

urlpatterns = [
    path('', PostListView.as_view(
        queryset=Post.objects.all().order_by("-date"),
        template_name='blog/blog.html',
        context_object_name='Posts',
        paginate_by=10
    ), name='blog'), 
    path('<int:pk>/', PostDetailView.as_view(
        model=Post,
        template_name='blog/blog.html'
    ), name='post'),
    
]
