# Generated by Django 2.2.6 on 2019-11-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0058_auto_20191125_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_group',
            name='users',
            field=models.ManyToManyField(to='accounts.Pair'),
        ),
        migrations.AlterField(
            model_name='group_transactions',
            name='group',
            field=models.ManyToManyField(to='accounts.Add_group'),
        ),
    ]