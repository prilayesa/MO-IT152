from django.urls import path
from . import views
from .views import UserListCreate, PostListCreate, CommentListCreate, LikesListCreate

urlpatterns = [
    # path('users/', views.get_users, name='get_users'),
    # path('users/create/', views.create_user, name='create_user'),
    # path('posts/', views.get_posts, name='get_posts'),
    # path('posts/create/', views.create_post, name='create_post'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    # As per milestone 2, the likes, comment and Google OAuth should be implemented.
    path('likes/', views.LikesListCreate.as_view(), name='likes-list-create'),
    path('likes/<int:pk>/', views.LikeDetail.as_view(), name='like-detail'),
]
