import shutil

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os

from src.base.services import get_path_upload_project_icon
from src.projects.models import ProjectFile, Projects


# @receiver(post_save)
# def my_callback(sender, instance: Projects, **kwargs):
#     saved_file = instance.icon
#     new_path = settings.MEDIA_ROOT.replace('\\', '/') + '/' + get_path_upload_project_icon(instance,
#                                                                         saved_file.name.split('/')[-1])
#     print(new_path)
#     shutil.move(instance.icon.path, new_path)
#
#     instance.file = saved_file
#     instance.save()
#     print(instance.icon)