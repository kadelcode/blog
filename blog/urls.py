from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post-create/', PostCreateView.as_view(), name='post_new'),
    path('edit-post/<int:pk>', PostUpdateView.as_view(), name='post_edit'),
    path('post-delete/<int:pk>', PostDeleteView.as_view(), name='post_delete')
]