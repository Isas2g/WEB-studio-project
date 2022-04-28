from django.db import models
from src.users.models import User


class Projects(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField()
    description = models.TextField()
    icon_url = models.TextField()
    creator = models.ManyToManyField(User,
                                     verbose_name="создатель",
                                     related_name="project_creator")

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Positions(models.Model):
    name = models.TextField()
    project = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.TextField()

    class Meta:
        db_table = 'positions'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class ProjectParticipants(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, null=True, blank=True)
    invited_at = models.DateTimeField()
    kicked_at = models.DateTimeField()

    class Meta:
        db_table = 'project_participant'
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'