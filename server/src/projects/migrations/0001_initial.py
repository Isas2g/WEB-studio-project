# Generated by Django 4.0.3 on 2022-04-26 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.BigIntegerField()),
                ('user_id', models.BigIntegerField()),
                ('position_id', models.BigIntegerField()),
                ('invited_at', models.DateTimeField()),
                ('kicked_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Участник проекта',
                'verbose_name_plural': 'Участники проекта',
                'db_table': 'project_participant',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('closed_at', models.DateTimeField()),
                ('description', models.TextField()),
                ('icon_url', models.TextField()),
                ('creator', models.ManyToManyField(related_name='project_creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='Postions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('color', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'db_table': 'positions',
            },
        ),
    ]
