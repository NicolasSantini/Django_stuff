from blog import views
from django.urls import path

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', views.add_comment_to_post.as_view(), name='add_comment_to_post'),
]
