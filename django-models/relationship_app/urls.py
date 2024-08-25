from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from relationship_app import views
from . import views
from .views import list_books, LibraryDetailView
from .views import librarian_view, member_view, register, admin_view, add_book, edit_book, delete_book


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', views.home, name='home'),          
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='templates/logout.html'), name='logout'),
    path('accounts/profile/', TemplateView.as_view(template_name = 'templates/profile.html'), name='profile'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('accounts/', include('django.contrib.auth.urls')),

    
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),

]








