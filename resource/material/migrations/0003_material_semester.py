# Generated by Django 3.2.5 on 2022-01-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_alter_material_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='semester',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
