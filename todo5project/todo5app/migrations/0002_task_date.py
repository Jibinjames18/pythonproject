# Generated by Django 4.2.1 on 2023-05-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo5app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-06-21'),
            preserve_default=False,
        ),
    ]
