# Generated by Django 2.2.3 on 2019-07-10 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_hit_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hit_count',
        ),
    ]
