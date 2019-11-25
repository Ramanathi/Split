# Generated by Django 2.2.6 on 2019-11-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20191123_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='group',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='split',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
