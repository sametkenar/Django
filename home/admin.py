from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','published','created')
    list_filter = ('published','created','author')
    search_fields = ('title','content')
    date_hierarchy = 'created'
    ordering = ('-created',)
    fieldsets = (
        (None, {'fields': ('title','content', 'author')}),
        ('Yayın', {'fields': ('published',)}),
        ('Tarih', {'fields': ('created', 'updated')}),
    )
    readonly_fields = ('created', 'updated')

    