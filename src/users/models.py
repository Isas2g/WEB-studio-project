from django.core.validators import FileExtensionValidator
from django.db.models import Model, ImageField, EmailField, DateTimeField
from django.db.models import CharField, ForeignKey, CASCADE

from .managers import CustomUserManager

from src.base.services import get_path_upload_avatar, validate_size_image


class Role(Model):
    title = CharField('название',
                      max_length=64,
                      unique=True
                      )

    class Meta:
        db_table = 'users_role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title


class CustomUsers(Model):
    username = CharField("ник",
                         max_length=150,
                         unique=True,
                         )

    email = EmailField(max_length=150,
                       unique=True,
                       )

    join_date = DateTimeField(auto_now_add=True,
                              )

    role = ForeignKey(Role,
                      on_delete=CASCADE,
                      blank=True,
                      null=True
                      )

    avatar = ImageField(upload_to=get_path_upload_avatar,
                        blank=True,
                        null=True,
                        validators=[
                            FileExtensionValidator(allowed_extensions=['jpg']),
                            validate_size_image
                        ]
                        )

    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return f'{self.username}:{self.role}'

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserContacts(Model):
    user = ForeignKey(CustomUsers,
                      on_delete=CASCADE
                      )

    title = CharField('название',
                      max_length=64,
                      unique=True,
                      )

    contact = CharField('контакт',
                        max_length=64,
                        unique=True,
                        )


    class Meta:
        db_table = 'users_contacts'
        verbose_name = 'Контакт Пользователя'
        verbose_name_plural = 'Контакты Пользователей'

    def __str__(self):
        return f'{self.user}:{self.title}:{self.contact}'
