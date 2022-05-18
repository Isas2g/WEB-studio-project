from django.contrib import admin
from .models import *

admin.site.register(Boards)
admin.site.register(TaskTags)
admin.site.register(Tasks)
admin.site.register(BoardColumns)
admin.site.register(BoardTasks)
admin.site.register(TaskComment)
