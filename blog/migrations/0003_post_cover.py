# Generated by Django 3.0.7 on 2020-06-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200616_0440'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
