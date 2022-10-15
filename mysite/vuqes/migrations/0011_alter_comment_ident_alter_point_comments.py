# Generated by Django 4.1.1 on 2022-09-29 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vuqes', '0010_alter_comment_ident_alter_point_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ident',
            field=models.TextField(default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='comments',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vuqes.comment'),
        ),
    ]