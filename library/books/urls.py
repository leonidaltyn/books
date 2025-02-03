from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book_list, name='book_list'),
    path('book/new/', views.book_new, name='post_new'),
    path('book/<int:pk>/', views.book_detail, name='book_detail')
]
