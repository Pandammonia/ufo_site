from django.contrib import admin
from .models import UserBlogPost

@admin.register(UserBlogPost)
class UserBlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'author', 'added', 'published', 'slug')
	prepopulated_fields = {'slug': ('title',)}
