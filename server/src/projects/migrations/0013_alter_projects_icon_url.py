# Generated by Django 4.0.3 on 2022-05-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_projectparticipants_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='icon_url',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
