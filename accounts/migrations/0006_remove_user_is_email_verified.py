# Generated by Django 3.2.5 on 2021-07-01 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_email_verified',
        ),
    ]
