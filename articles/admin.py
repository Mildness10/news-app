from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

#registering the article model in the admin page
admin.site.register(Article)

#registering the comment model in the admin page
admin.site.register(Comment)
