# Generated by Django 2.2.3 on 2019-07-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('ssid', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30)),
                ('encryption', models.CharField(max_length=30)),
            ],
        ),
    ]
