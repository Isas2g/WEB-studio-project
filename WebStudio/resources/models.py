from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import ImageField, ForeignKey, CASCADE
from django.db.models import Model, CharField

from resources.managers import CustomUserManager


class Role(Model):
    title = CharField(
        'название',
        max_length=64,
        unique=True
    )

    class Meta:
        db_table = 'role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title


class CustomUsers(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = CharField(
        "ник",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )

    role = ForeignKey(Role, on_delete=CASCADE)

    avatar = ImageField(upload_to='user/avatar/', blank=True, null=True)
    first_name = None
    last_name = None

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}:{self.role}'


class Posts(Model):
    title = CharField(
        'название',
        max_length=64,
        unique=True,
    )

    class Meta:
        db_table = 'post'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title


class UserContacts(Model):
    user = CustomUsers
    title = CharField(
        'название',
        max_length=64,
        unique=True,
    )
    contact = CharField(
        'контакт',
        max_length=64,
        unique=True,
    )

    class Meta:
        db_table = 'human_contacts'
        verbose_name = 'Контакт Пользователя'
        verbose_name_plural = 'Контакты Пользователей'

    def __str__(self):
        return f'{self.user}:{self.title}:{self.contact}'


class Projects(Model):
    id = models.BigIntegerField()
    title = models.TextField()
    created_at = models.DateTimeField()
    closed_at = models.DateTimeField()
    description = models.TextField()
    icon_url = models.TextField()
    creator_id = models.ManyToManyField(CustomUsers, verbose_name="создатель", related_name="project_creator")

    class Meta:
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Boards(Model):
    id = models.BigIntegerField()
    title = models.TextField()
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'boards'
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'


class ProjectParticipants(Model):
    project_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    position_id = models.BigIntegerField()
    invited_at = models.DateTimeField()
    kicked_at = models.DateTimeField()

    class Meta:
        db_table = 'project_participant'
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'


class Postions(Model):
    id = models.BigIntegerField()
    name = models.TextField()
    project_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    color = models.TextField()

    class Meta:
        db_table = 'positions'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class TaskTags(Model):
    id = models.BigIntegerField()
    text = models.TextField()
    color = models.TextField()

    class Meta:
        db_table = 'task_tags'
        verbose_name = 'Ярлык'
        verbose_name_plural = 'Ярлыки'


class Tasks(Model):
    id = models.BigIntegerField()
    title = models.TextField()
    description = models.TextField()
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    is_done = models.BooleanField()
    executor_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    done_at = models.DateTimeField()
    author_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(TaskTags, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class BoardColumns(Model):
    id = models.BigIntegerField()
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)
    title = models.TextField()
    creator_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)

    class Meta:
        db_table = 'board_columns'
        verbose_name = 'Колонка доски'
        verbose_name_plural = 'Колонки досок'


class BoardTasks(Model):
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    column_id = models.ForeignKey(BoardColumns, on_delete=models.CASCADE)

    class Meta:
        db_table = 'board_tasks'
        verbose_name = 'Задача доски'
        verbose_name_plural = 'Задачи досок'


class Backups(Model):
    id = models.BigIntegerField()
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'backups'
        verbose_name = 'Резервная копия'
        verbose_name_plural = 'Резервные копии'


class TaskComment(Model):
    id = models.BigIntegerField()
    content = models.TextField()
    created_at = models.DateTimeField()
    author_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    is_reply = models.BooleanField()
    # reply_comment_id = models.ForeignKey(TaskComment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'task_comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


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