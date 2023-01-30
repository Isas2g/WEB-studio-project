from django.core.validators import FileExtensionValidator
import os
from django.db import models
from django.conf import settings

from ..base.services import validate_size_image, \
    get_path_upload_project_icon, get_path_upload_project_files
from ..users.models import User


class Projects(models.Model):
    title = models.CharField(max_length=64)
    created_at = models.DateField()
    closed_at = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to=get_path_upload_project_icon,
                             null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['jpg']),
                                 validate_size_image
                             ])
    creator = models.ForeignKey(User, verbose_name="создатель", related_name="project_creator",
                                on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class ProjectFile(models.Model):
    title = models.CharField("Название", max_length=255)
    file = models.FileField("Файл",
                            upload_to=get_path_upload_project_files,
                            validators=[FileExtensionValidator(
                                allowed_extensions=['txt, doc, docx, pdf, xlsx'])]
                            )
    project = models.ForeignKey("Projects", on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return self.title

class ProjectFeedback(models.Model):
    username = models.CharField('ник',
                                max_length=150)

    CHOISE_ESTIMATION = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    estimation = models.IntegerField(choices=CHOISE_ESTIMATION)

    comment = models.TextField(blank=True, null=True)

    project = models.ForeignKey(Projects, 
                                on_delete=models.CASCADE, 
                                blank=True, 
                                )

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
