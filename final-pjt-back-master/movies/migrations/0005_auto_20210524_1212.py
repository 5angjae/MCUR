# Generated by Django 3.2.3 on 2021-05-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210524_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='cookie_movie_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='type',
            field=models.CharField(default='movie', max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tmdb_id',
            field=models.IntegerField(default=0),
        ),
    ]
