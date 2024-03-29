# Generated by Django 4.0.3 on 2022-05-27 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0009_remove_projects_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='project_creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
    ]
