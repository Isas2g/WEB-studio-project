from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import Model, ImageField
from django.db.models import CharField, ForeignKey, CASCADE

from users.managers import CustomUserManager


class Role(Model):
    title = CharField(
        'название',
        max_length=64,
        unique=True
    )

    class Meta:
        db_table = 'users_role'
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
            "unique": "A users with that username already exists.",
        },
    )

    role = ForeignKey(Role, on_delete=CASCADE, blank=True, null=True)

    avatar = ImageField(upload_to='users/avatar/', blank=True, null=True)
    first_name = None
    last_name = None

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}:{self.role}'


class UserContacts(Model):
    user = ForeignKey(CustomUsers, on_delete=CASCADE)
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
        db_table = 'users_contacts'
        verbose_name = 'Контакт Пользователя'
        verbose_name_plural = 'Контакты Пользователей'

    def __str__(self):
        return f'{self.user}:{self.title}:{self.contact}'

