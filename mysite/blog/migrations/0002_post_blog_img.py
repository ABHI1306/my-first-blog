# Generated by Django 3.2.6 on 2021-08-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
