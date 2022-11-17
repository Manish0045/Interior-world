# Generated by Django 4.0.4 on 2022-08-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.EmailField(max_length=30)),
                ('unm', models.CharField(max_length=10)),
                ('pwd', models.CharField(max_length=8)),
                ('pwd1', models.CharField(max_length=8)),
            ],
        ),
    ]
