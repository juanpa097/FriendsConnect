# Generated by Django 2.1 on 2018-09-07 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('due_date', models.DateTimeField()),
                ('max_participants', models.IntegerField()),
                ('visibility', models.BooleanField()),
            ],
        ),
    ]