# Generated by Django 3.2.4 on 2024-01-30 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default='10hrs', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='course',
            name='season',
            field=models.CharField(choices=[('', 'Select Season'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn')], default='', max_length=25),
        ),
    ]
