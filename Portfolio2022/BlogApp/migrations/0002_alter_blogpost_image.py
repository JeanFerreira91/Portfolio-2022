# Generated by Django 4.0.4 on 2022-04-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='', upload_to='BlogApp/static/BlogApp/static/img'),
        ),
    ]
