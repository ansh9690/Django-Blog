from django.contrib import admin
from .models import Post, BlogComment

admin.site.register(BlogComment)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'timeStamp')
    list_filter = ("title",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'sno': ('title',)}


admin.site.register(Post, PostAdmin)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     class Media:
#         js = 'textEditor.js',
