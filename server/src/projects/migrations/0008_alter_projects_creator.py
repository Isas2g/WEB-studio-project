# Generated by Django 4.0.3 on 2022-05-19 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_remove_projects_creator_projects_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
    ]
