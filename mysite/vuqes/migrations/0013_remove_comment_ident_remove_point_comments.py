# Generated by Django 4.1.1 on 2022-09-29 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vuqes', '0012_alter_point_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='ident',
        ),
        migrations.RemoveField(
            model_name='point',
            name='comments',
        ),
    ]