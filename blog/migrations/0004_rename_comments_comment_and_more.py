# Generated by Django 4.1 on 2023-10-31 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comments_comments_blog_commen_created_ad0231_idx'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameIndex(
            model_name='comment',
            new_name='blog_commen_created_0e6ed4_idx',
            old_name='blog_commen_created_ad0231_idx',
        ),
    ]
