from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField


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
