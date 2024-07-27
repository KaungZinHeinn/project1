from django.urls import path
from .views import category_list, category_create, category_detail, category_update, category_delete, post_list

urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/create/', category_create, name='category-create'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('categories/<int:pk>/update/', category_update, name='category-update'),
    path('categories/<int:pk>/delete/', category_delete, name='category-delete'),
    path('post/', post_list, name='post-list'),
    
]
