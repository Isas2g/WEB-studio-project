# Generated by Django 4.0.3 on 2022-05-25 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_post_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='disabled_at',
            field=models.DateTimeField(null=True, verbose_name='время заморозки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='post',
            field=models.CharField(blank=True, choices=[('designer', 'Дизайнер'), ('backend', 'Бэк'), ('frontend', 'Фронт'), ('manager', 'Менеджер')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userrole'),
        ),
    ]
