# Generated by Django 4.0.3 on 2022-04-26 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='access_level',
            field=models.IntegerField(default=500, verbose_name='уровень доступа'),
        ),
    ]