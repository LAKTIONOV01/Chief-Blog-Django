from django import template
from ..models import Categories, Post, Photo

register = template.Library()


# Displaying categories
@register.simple_tag()
def get_categories():
    return Categories.objects.all()


# Last 5 posts
@register.inclusion_tag('blog/include/tags/posts_menu.html')
def get_last_posts():
    posts = Post.objects.order_by('-id')[:5]
    return {'last_posts': posts}


# Making a carousel from post photos
@register.inclusion_tag('blog/include/tags/gallery_menu.html')
def get_gallery():
    photos = Photo.objects.order_by('-id')[:8]
    return {'photos': photos}
