from django.contrib import admin
from post.models import Post, Like


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'user')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
