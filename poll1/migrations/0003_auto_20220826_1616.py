# Generated by Django 3.2.12 on 2022-08-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll1', '0002_auto_20220823_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='re',
            name='votes',
        ),
        migrations.AddField(
            model_name='re',
            name='vote1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='re',
            name='vote2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='re',
            name='vote3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='re',
            name='vote4',
            field=models.IntegerField(default=0, null=True),
        ),
    ]