# Generated by Django 3.2 on 2021-04-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageModel', '0005_styleimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='styleimg',
            name='img',
            field=models.ImageField(upload_to='style_img'),
        ),
    ]
