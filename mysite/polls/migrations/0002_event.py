# Generated by Django 2.2.1 on 2019-06-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=20)),
                ('latitude', models.IntegerField(default=0)),
                ('longitude', models.IntegerField()),
            ],
        ),
    ]
