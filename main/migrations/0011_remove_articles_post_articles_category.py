# Generated by Django 5.1.7 on 2025-03-23 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_post_category_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='post',
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='main.categories'),
        ),
    ]
