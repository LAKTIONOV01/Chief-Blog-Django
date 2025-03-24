from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
import datetime


# Create your models here.

class Categories(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'Category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'Tag'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/')
    category = models.ForeignKey(Categories, related_name='posts', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, related_name='post')
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', max_length=200)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_recipes(self):
        return self.recipes.all()

    def get_comments(self):
        return self.comment.all()


class Articles(models.Model):
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Categories, related_name='articles', on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("main:post_list", kwargs={"slug": self.category.slug})


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(Post, related_name='recipes', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        db_table = 'Recipe'

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=datetime.datetime.now)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сomment'
        verbose_name_plural = 'Comments'
        db_table = 'Comment'

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    captions = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'gallery'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'