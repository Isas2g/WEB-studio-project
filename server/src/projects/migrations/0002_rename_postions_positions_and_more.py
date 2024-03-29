# Generated by Django 4.0.3 on 2022-04-27 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postions',
            new_name='Positions',
        ),
        migrations.RemoveField(
            model_name='projectparticipants',
            name='position_id',
        ),
        migrations.RemoveField(
            model_name='projectparticipants',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='projectparticipants',
            name='user_id',
        ),
        migrations.AddField(
            model_name='projectparticipants',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.positions'),
        ),
        migrations.AddField(
            model_name='projectparticipants',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
        migrations.AddField(
            model_name='projectparticipants',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
