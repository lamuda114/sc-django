from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_public', 'created_at']
    list_display_links = ['title']    #타이틀에 링크 달기
    list_editable = ['is_public']    #체크박스로 변환

admin.site.register(Post, PostAdmin)
