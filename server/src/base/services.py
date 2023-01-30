from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    return f'avatar/{instance.username}/{file}'


def get_path_upload_project_icon(instance, file):
    return f'project/icon/{instance}/{file}'

def get_path_upload_project_files(instance, file):
    return f'project/files/{instance}/{file}'


def validate_size_image(file_obj):
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}МБ")


