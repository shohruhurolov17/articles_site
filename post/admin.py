from django.contrib import admin
from .models import Comment, Post
# Register your models here.


class CommentLines(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentLines]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
