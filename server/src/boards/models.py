from django.db import models
from src.projects.models import Projects
from src.users.models import User


class Boards(models.Model):
    title = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'boards'
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.title


class TaskTags(models.Model):
    text = models.TextField()
    color = models.TextField()

    class Meta:
        db_table = 'task_tags'
        verbose_name = 'Ярлык'
        verbose_name_plural = 'Ярлыки'

    def __str__(self):
        return self.text


class Tasks(models.Model):
    title = models.TextField()
    description = models.TextField()
    board = models.ForeignKey(Boards, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    is_done = models.BooleanField()
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='executor')
    done_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    tag = models.ForeignKey(TaskTags, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title


class BoardColumns(models.Model):
    board = models.ForeignKey(Boards, on_delete=models.CASCADE)
    title = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'board_columns'
        verbose_name = 'Колонка доски'
        verbose_name_plural = 'Колонки досок'

    def __str__(self):
        return self.title


class BoardTasks(models.Model):
    board = models.ForeignKey(Boards, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    column = models.ForeignKey(BoardColumns, on_delete=models.CASCADE)

    class Meta:
        db_table = 'board_tasks'
        verbose_name = 'Задача доски'
        verbose_name_plural = 'Задачи досок'

    def __str__(self):
        return self.board.title


class TaskComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    is_reply = models.BooleanField()
    reply_comment = models.ForeignKey('TaskComment', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'task_comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.author.username
