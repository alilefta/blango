from django.contrib import admin
from .models import Tag, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['slug', 'published_at']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)