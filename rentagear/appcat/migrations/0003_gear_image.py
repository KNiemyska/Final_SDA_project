# Generated by Django 2.2.12 on 2020-07-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcat', '0002_auto_20200725_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
