# Generated by Django 3.2.12 on 2022-08-29 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll1', '0012_auto_20220829_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='user',
        ),
        migrations.DeleteModel(
            name='re',
        ),
        migrations.DeleteModel(
            name='votes',
        ),
    ]
