# Generated by Django 5.1.5 on 2025-02-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetable', '0002_alter_receipe_receipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(upload_to='receipe'),
        ),
    ]
