# Generated by Django 3.2.5 on 2021-07-15 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210715_2204'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]