# Generated by Django 2.2.3 on 2019-08-05 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='images',
        ),
    ]
