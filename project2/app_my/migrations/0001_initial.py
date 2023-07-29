# Generated by Django 4.2.2 on 2023-06-20 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=25)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]
