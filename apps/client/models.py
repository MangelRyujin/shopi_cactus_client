from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, first_name, last_name, password, is_staff, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_user(self, username, email, first_name, last_name, password = None, **extra_fields):
        return self._create_user(username, email, first_name, last_name, password , False ,**extra_fields)
    
    def create_superuser(self, username, email, first_name, last_name, password = None, **extra_fields):
        pass
    
class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField('Correo Electrónico', max_length=255 , unique=True, blank = False, null= False)
    first_name = models.CharField('Nombre', max_length=255, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    
    class Meta:    
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name','last_name']
    
    def natural_key(self):
        return (self.username)
    
    def __str__(self) -> str:
        return f'{self.first_name}  {self.last_name}'
    