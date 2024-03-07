from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)