# Generated by Django 4.1.1 on 2022-09-29 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vuqes', '0009_comment_ident_point_comments_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ident',
            field=models.TextField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='comments',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='vuqes.comment'),
        ),
    ]