# Generated by Django 3.2 on 2021-04-26 13:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ImageModel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='img_url',
        ),
        migrations.AddField(
            model_name='img',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='upload'),
            preserve_default=False,
        ),
    ]
