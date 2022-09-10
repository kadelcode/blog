from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post-create/', PostCreateView.as_view(), name='post_new'),
]