# Generated by Django 4.2.7 on 2024-01-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='未定義のイベント', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='map_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='store_link',
            field=models.URLField(blank=True),
        ),
    ]
