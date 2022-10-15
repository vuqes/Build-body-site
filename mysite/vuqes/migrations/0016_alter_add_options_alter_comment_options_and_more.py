# Generated by Django 4.1.1 on 2022-10-04 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vuqes', '0015_writetotraining_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='add',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['comment', 'date'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AlterModelOptions(
            name='point',
            options={'ordering': ['pub_date', 'title'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='point',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vuqes.add', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='point',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='writetotraining',
            name='datetime',
            field=models.DateTimeField(blank=True, verbose_name='Дата записи'),
        ),
        migrations.AlterField(
            model_name='writetotraining',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='writetotraining',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='writetotraining',
            name='phone_number',
            field=models.CharField(max_length=200, verbose_name='Номер телефона '),
        ),
    ]
