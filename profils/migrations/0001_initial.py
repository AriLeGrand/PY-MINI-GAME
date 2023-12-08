# Generated by Django 5.0 on 2023-12-08 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('time', models.DateTimeField(verbose_name='')),
            ],
        ),
    ]
