# Generated by Django 3.1 on 2023-09-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
