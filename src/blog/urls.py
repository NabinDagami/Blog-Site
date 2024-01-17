from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name='index'),
    path('blog/blog-list/', views.blog_list, name='blog-list'),
    path('blog/author-list/', views.author_list, name='author-list'),
    path('blog/author/<int:author_id>/', views.author_detail, name='author-detail'),
    path('blog/detail/<int:blog_id>/', views.blog_detail, name='blog-detail'),
    path('blog/update-blog/<int:blog_id>/', views.update_blog, name='update-blog'),
    path('blog/delete-blog/<int:blog_id>/', views.delete_blog, name='delete-blog'),
    path('blog/add-blog/', views.add_blog, name='add-blog'),
]
