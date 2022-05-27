# Generated by Django 4.0.3 on 2022-05-27 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_projects_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positions',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
        migrations.AlterField(
            model_name='projectparticipants',
            name='kicked_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='icon_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]