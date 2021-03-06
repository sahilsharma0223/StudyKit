# Generated by Django 3.2.5 on 2022-01-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0004_alter_material_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='material/document'),
        ),
        migrations.AlterField(
            model_name='material',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='material/video'),
        ),
    ]
