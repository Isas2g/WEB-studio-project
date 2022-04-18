from django.db import models
from projects.models import Projects
from users.models import CustomUsers


class Boards(models.Model):
    id = models.BigIntegerField()
    title = models.TextField()
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    class Meta:
        db_table = 'boards'
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'


class TaskTags(models.Model):
    id = models.BigIntegerField()
    text = models.TextField()
    color = models.TextField()

    class Meta:
        db_table = 'task_tags'
        verbose_name = 'Ярлык'
        verbose_name_plural = 'Ярлыки'


class Tasks(models.Model):
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


class BoardColumns(models.Model):
    id = models.BigIntegerField()
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)
    title = models.TextField()
    creator_id = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)

    class Meta:
        db_table = 'board_columns'
        verbose_name = 'Колонка доски'
        verbose_name_plural = 'Колонки досок'


class BoardTasks(models.Model):
    board_id = models.ForeignKey(Boards, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    column_id = models.ForeignKey(BoardColumns, on_delete=models.CASCADE)

    class Meta:
        db_table = 'board_tasks'
        verbose_name = 'Задача доски'
        verbose_name_plural = 'Задачи досок'


class TaskComment(models.Model):
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