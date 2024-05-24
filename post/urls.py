from django.urls import path
from .views import (
PostCreateView,
PostDetailView,
PostListView,
PostUpdateView,
PostRemoveView,
CommentCreateView,
CommentUpdateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/remove', PostRemoveView.as_view(), name='post_remove'),
    path('<int:pk>/comment/create/', CommentCreateView.as_view(), name='post_create_comment'),
    path('<int:pk>/comment/<int:comment_pk>/update', CommentUpdateView.as_view(), name='comment-update'),

]