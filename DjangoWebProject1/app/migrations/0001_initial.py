# Generated by Django 4.2.6 on 2024-01-18 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='title1')),
                ('description', models.TextField(verbose_name='content 1')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2024, 1, 18, 11, 54, 35, 721551), verbose_name='Опубликована')),
            ],
        ),
    ]