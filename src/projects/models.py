from django.db import models
from src.users.models import CustomUsers



class Projects(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField()
    description = models.TextField()
    icon_url = models.TextField()
    creator_id = models.ManyToManyField(CustomUsers,
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
    project_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    color = models.TextField()

    class Meta:
        db_table = 'positions'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class ProjectParticipants(models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    position_id = models.ForeignKey(Positions, on_delete=models.CASCADE)
    invited_at = models.DateTimeField()
    kicked_at = models.DateTimeField()

    class Meta:
        db_table = 'project_participant'
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'