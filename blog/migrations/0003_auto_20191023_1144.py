# Generated by Django 2.2.3 on 2019-10-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_blood_sugar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blood_sugar',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.IntegerField(),
        ),
    ]
