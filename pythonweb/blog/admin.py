from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    list_display=['title','date']
    list_filter = ['date']
    search_fields= ['title']
    
admin.site.register(Post, PostAdmin)
# Register your models here.
