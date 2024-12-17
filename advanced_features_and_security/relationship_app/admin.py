from django.contrib import admin
from .models import Author, Book, Library, Librarian, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register other models
admin.site.register((Author, Book, Library, Librarian))

# Define the CustomUser admin class
class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')

# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
