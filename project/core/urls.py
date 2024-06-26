# urls.py

from django.urls import path
from .views import HomeView, PostView, PostCreateView, PostUpdateView, TagFilterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<pk>/<slug:slug>/', PostView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('tag/<slug:tag_slug>/', TagFilterView.as_view(), name='tag_filter'),
    path('post/<pk>/<slug:slug>/', PostView.as_view(), name='post_detail'),
]
