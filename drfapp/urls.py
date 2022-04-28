from django.template import base
from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, CommentViewset

post_router = routers.SimpleRouter(trailing_slash=False)
post_router.register(r'posts', PostViewSet, basename='post')

comment_router = routers.SimpleRouter(trailing_slash=False)
comment_router.register(r'comments', CommentViewset, basename='comment')


urlpatterns = [
    path('', include(post_router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),
]
