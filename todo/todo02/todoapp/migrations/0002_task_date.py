# Generated by Django 3.2.15 on 2022-08-24 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-02-24'),
            preserve_default=False,
        ),
    ]
