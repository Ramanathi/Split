# Generated by Django 2.2.7 on 2019-11-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20191123_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/1.jpg', null=True, upload_to='images/'),
        ),
    ]
