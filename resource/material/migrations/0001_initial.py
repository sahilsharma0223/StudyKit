# Generated by Django 3.2.5 on 2022-01-18 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, upload_to='material/thumbnail')),
                ('link', models.URLField(blank=True)),
                ('document', models.FileField(blank=True, upload_to='material/document')),
                ('video', models.FileField(blank=True, upload_to='material/video')),
                ('like_count', models.IntegerField(default=0)),
                ('dislike_count', models.IntegerField(default=0)),
            ],
        ),
    ]