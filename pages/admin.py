from django.contrib import admin
from .models import Theory, Sighting, BlogPost

admin.site.register(Theory)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'username', 'added', 'published', 'slug')
	prepopulated_fields = {'slug': ('title',)}

@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
	list_display = ['subj', 'body', 'location', 'added', 'time_of', 'name', 'slug']
	prepopulated_fields = {'slug': ('subj',)}


