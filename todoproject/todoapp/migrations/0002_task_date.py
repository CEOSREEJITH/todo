# Generated by Django 3.2.15 on 2022-10-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1995-05-09'),
            preserve_default=False,
        ),
    ]
