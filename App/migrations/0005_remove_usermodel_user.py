# Generated by Django 2.1 on 2018-10-13 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20181013_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='user',
        ),
    ]
