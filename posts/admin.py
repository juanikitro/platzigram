# Django
from django.contrib import admin

# Posts
from posts.models import Posts


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'photo', )


admin.site.register(Posts, PostAdmin)