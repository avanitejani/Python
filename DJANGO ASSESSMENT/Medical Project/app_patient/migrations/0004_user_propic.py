# Generated by Django 4.2.3 on 2023-07-26 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_patient', '0003_remove_user_cpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='propic',
            field=models.FileField(default='anonymous.jpg', upload_to='media/'),
        ),
    ]
