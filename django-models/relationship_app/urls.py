from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Home view
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]


urlpatterns = [
    # Other URL patterns
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('member/', views.member_view, name='member'),
]

from django.urls import path
from .views import home, librarian_view, member_view, register

urlpatterns = [
    path('', home, name='home'),  # Home page URL pattern
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    path('register/', register, name='register'),  # Registration URL pattern
    # Add other URL patterns here
]
