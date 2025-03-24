from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe


# Register your models here.


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Categories)
class CategoriesAdmin(MPTTModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'serves', 'prep_time', 'cook_time']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'text', 'author', 'slug', 'get_image']
    readonly_fields = ['get_image']
    inlines = [RecipeInline]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="100" ')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_date', 'get_image']
    readonly_fields = ['get_image']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="100" ')

admin.site.register(Articles)
