# Generated by Django 3.0.5 on 2020-05-19 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_auto_20200520_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='active',
        ),
    ]