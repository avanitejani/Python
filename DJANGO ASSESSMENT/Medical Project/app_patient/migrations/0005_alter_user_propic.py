# Generated by Django 4.2.3 on 2023-07-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_patient', '0004_user_propic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='propic',
            field=models.FileField(default='anonymous.png', upload_to='media/'),
        ),
    ]
