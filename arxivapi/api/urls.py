from django.urls import path

from . import views

urlpatterns = [
    path('papers', views.paper_list, name='paper_list'),
    path('papers/<int:id>', views.paper_detail, name='paper_detail'),
    path('authors', views.author_list, name='author_list'),
    path('authors/<int:id>', views.author_detail, name='author_detail'),
    path('categories', views.category_list, name='category_list'),
    path('categories/<int:id>', views.category_detail, name='category_detail'),
]
