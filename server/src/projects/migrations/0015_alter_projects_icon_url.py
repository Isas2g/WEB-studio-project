# Generated by Django 4.0.3 on 2022-05-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_projects_icon_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='icon_url',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]
