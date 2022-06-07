# Generated by Django 4.0.3 on 2022-06-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0007_alter_boards_ended_at_alter_boards_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='boards',
            name='ended_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='updated_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='done_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
