# Generated by Django 4.0.4 on 2022-05-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vede',
            field=models.FileField(null=True, upload_to='file deta'),
        ),
    ]
