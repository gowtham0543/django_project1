from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('blog/add', views.post_add, name='post_add'),
    path('blog/<int:post_id>/', views.post_detail, name='post_detail'),
    path('blog/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('blog/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('blog/search/', views.search_view, name='search_view'),
]