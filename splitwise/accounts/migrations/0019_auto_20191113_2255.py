# Generated by Django 2.2.6 on 2019-11-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_add_group_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_group',
            name='user',
        ),
        migrations.CreateModel(
            name='group_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(to='accounts.add_group')),
            ],
        ),
    ]
