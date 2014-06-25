from django.contrib import admin
from blog.models import *

# Register your models here.
class AuthorInline(admin.TabularInline):
    model = Author
    extra = 1
class ClassificationInline(admin.TabularInline):
    model = Classification
    extra = 1
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name',)
class ArticleAdmin(admin.ModelAdmin):
    """
    fieldsets = [
        ('Article', {'fields': ['capture']}),
    ]
    """
    list_display = ('caption', 'subcaption', 'author')
    #inlines = [AuthorInline, ClassificationInline]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Author, AuthorAdmin)
