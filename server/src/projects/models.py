from django.db import models

from ..users.models import User


class Projects(models.Model):
    title = models.CharField(max_length=64)
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon_url = models.ImageField(upload_to='images/', blank=True, null=True)
    creator = models.ForeignKey(User, verbose_name="создатель", related_name="project_creator",
                                on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Positions(models.Model):
    name = models.CharField(max_length=64)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True, null=True)
    color = models.CharField(max_length=32)

    class Meta:
        db_table = 'positions'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class ProjectParticipants(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, null=True, blank=True)
    invited_at = models.DateTimeField()
    kicked_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'project_participant'
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'

    def __str__(self):
        return self.project.title
