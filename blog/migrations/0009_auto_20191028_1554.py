# Generated by Django 2.2.3 on 2019-10-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20191028_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=0, max_length=500, verbose_name='Information'),
        ),
    ]