# Generated by Django 3.2.12 on 2022-08-27 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll1', '0005_auto_20220827_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll1.re')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll1.ques')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='vote',
        ),
    ]