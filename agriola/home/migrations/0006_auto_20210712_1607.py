# Generated by Django 3.2.3 on 2021-07-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_image_imagemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='images',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='input1',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='input2',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
    ]
