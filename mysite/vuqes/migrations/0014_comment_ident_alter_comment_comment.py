# Generated by Django 4.1.1 on 2022-09-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuqes', '0013_remove_comment_ident_remove_point_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ident',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=200, verbose_name='Оставить комментарий '),
        ),
    ]
