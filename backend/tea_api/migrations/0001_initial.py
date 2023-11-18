# Generated by Django 4.2.7 on 2023-11-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.TextField()),
                ('altnames', models.TextField()),
                ('origin', models.TextField()),
                ('caffeine', models.CharField()),
                ('caffeineLevel', models.TextField()),
                ('description', models.CharField()),
                ('colorDescription', models.CharField()),
                ('tasteDescription', models.CharField()),
            ],
        ),
    ]
