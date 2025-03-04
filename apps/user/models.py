from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.timezone import now


class UserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError("올바른 이메일을 입력하세요.")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_active = False
        user.save()
        return user

    # 슈퍼 사용자 생성 , python manage.py createsuperuser
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", unique=True)
    nickname = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    last_login = models.DateTimeField(default=now)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = f"{verbose_name} 목록"

    def get_full_name(self):
        return self.nickname

    def get_short_name(self):
        return self.nickname

    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin
