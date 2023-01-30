from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.core.validators import FileExtensionValidator
from django.db.models import CharField, ForeignKey, CASCADE, BooleanField, IntegerField
from django.db.models import Model, ImageField, EmailField, DateTimeField, Choices

from src.base.services import get_path_upload_avatar, validate_size_image
from .managers import CustomUserManager
from django.conf import settings


# AbstractUser


class UserRole(Model):
    title = CharField('название',
                      max_length=64,
                      unique=True,
                      default='работяга')
    access_level = IntegerField('уровень доступа', default=500)

    class Meta:
        db_table = 'users_role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title


class User(AbstractBaseUser, PermissionsMixin):
    username = CharField("ник",
                         max_length=150,
                         unique=True,
                         )

    email = EmailField(max_length=150,
                       unique=True,
                       )

    join_date = DateTimeField(auto_now_add=True)

    role = ForeignKey(UserRole,
                      on_delete=CASCADE,
                      null=True
                      )

    position = CharField(max_length=25,
                         choices=settings.POSITIONS,
                         null=True)

    avatar = ImageField(upload_to=get_path_upload_avatar,
                        null=True,
                        validators=[
                            FileExtensionValidator(allowed_extensions=['jpg']),
                            validate_size_image
                        ]
                        )

    disabled_at = DateTimeField("время заморозки",
                                null=True,
                                )

    is_staff = BooleanField(
        "staff status",
        default=False,
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return True

    def __str__(self):
        return f'{self.username}:{self.role}'

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserContact(Model):
    user = ForeignKey(User,
                      on_delete=CASCADE,
                      related_name='contacts')

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
