# Generated by Django 3.2.4 on 2024-02-02 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_in_focus', '0005_alter_plantinfocus_featured_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantinfocus',
            name='featured_item_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
