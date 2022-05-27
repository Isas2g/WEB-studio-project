# Generated by Django 4.0.3 on 2022-05-19 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_positions_project_alter_projects_description'),
        ('boards', '0005_alter_tasks_board_alter_tasks_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
    ]
