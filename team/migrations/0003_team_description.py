# Generated by Django 3.0.2 on 2020-04-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20200117_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(default='I Can do anything', max_length=1000),
        ),
    ]
