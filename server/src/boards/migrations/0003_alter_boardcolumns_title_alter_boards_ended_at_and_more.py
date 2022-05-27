# Generated by Django 4.0.3 on 2022-05-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_taskcomment_reply_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardcolumns',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='boards',
            name='ended_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='boards',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='is_reply',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='taskcomment',
            name='updated_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='done_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='tasktags',
            name='color',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='tasktags',
            name='text',
            field=models.CharField(max_length=64),
        ),
    ]
