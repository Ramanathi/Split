# Generated by Django 2.2.7 on 2019-11-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20191114_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='accounts/media/images/1.jpg', upload_to='images/'),
        ),
    ]
