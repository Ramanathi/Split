# Generated by Django 2.2.6 on 2019-11-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20191124_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_group',
            name='users',
            field=models.ManyToManyField(to='accounts.Pair'),
        ),
        migrations.AlterField(
            model_name='group_transactions',
            name='amt_for_him',
            field=models.CharField(blank=True, default='', max_length=10000000),
        ),
        migrations.AlterField(
            model_name='group_transactions',
            name='group',
            field=models.ManyToManyField(to='accounts.Add_group'),
        ),
    ]
