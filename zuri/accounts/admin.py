from django.contrib import admin
from .models import User, Product , Platform, Comment

# Register your models here.
admin.site.register(User)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =  ('username','product','created','active')
    list_filter = ('active' , 'created')
    search_fields = ('username', 'product','body')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name','id')

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'product','price')
    list_filter = ['price']
    search_fields = ['name']