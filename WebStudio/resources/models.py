from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField
from django.db import models
from WebStudio.boards.models import Boards

# Create your models here.

class CustomUsers(AbstractUser):
    pass


class Posts(Model):
    title = CharField(
        max_length=64,
        unique=True,
        verbose_name='название'
    )

    class Meta:
        db_table = 'post'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title


class HumanContacts(Model):
    user = CustomUsers
    title = CharField(
        max_length=64,
        unique=True,
        verbose_name='название'
    )
    contact = CharField(
        max_length=64,
        unique=True,
        verbose_name='контакт'
    )

    class Meta:
        db_table = 'human_contacts'
        verbose_name = 'Контакт Пользователя'
        verbose_name_plural = 'Контакты Пользователей'

    def __str__(self):
        return f'{self.user}:{self.title}:{self.contact}'


class FilesProjects(Model):
    title = CharField(
        max_length=64,
        unique=True,
        verbose_name='название'
    )
    file = CharField(
        max_length=64,
        unique=True,
        verbose_name='файл'
    )


class Backups(Model):
    id = models.BigIntegerField()
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'backups'
        verbose_name = 'Резервная копия'
        verbose_name_plural = 'Резервные копии'


class UserContacts(Model):
    user_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    contact_name = models.TextField()
    link = models.TextField()

    class Meta:
        db_table = 'user_contacts'
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class UserRoles(Model):
    id = models.BigIntegerField()
    title = models.TextField()
    access_level = models.BigIntegerField()

    class Meta:
        db_table = 'user_roles'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Forms(Model):
    id = models.BigIntegerField()
    name = models.TextField()
    surname = models.TextField()
    course = models.TextField()
    group = models.TextField()
    about_me = models.TextField()
    position = models.TextField()
    created_at = models.DateTimeField()
    denied_at = models.DateTimeField()
    is_accepted = models.DateTimeField()

    class Meta:
        db_table = 'forms'
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'