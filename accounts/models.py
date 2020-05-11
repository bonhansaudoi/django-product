from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import ( 
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserAccountManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        # if not email:
        #     raise ValueError('Yêu cầu email!')
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
 
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField( 
        # 'Tên', 
        max_length=30, 
        blank=True, null=True
    )
    # last_name = models.CharField( 
    #     # 'Họ', 
    #     max_length=50, 
    #     blank=True, null=True
    # )
    avatar = models.ImageField(
        # 'Ảnh cá nhân',
        default='avatar.jpg', 
        upload_to='profile',
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

    objects = UserAccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email