
from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .validators import ValidateEmail

# Create your models here.
class CustomUserManager(UserManager):
    '''
    overiding the default django case sensistive username check
    '''
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field:username})


class User(AbstractUser):
    
    '''
    User model by default inherits from the Abstract Base class the following required fields (username and password)
    Adds email fields to the User model
    
    '''
    # use new manager
    objects = CustomUserManager()

    # add unique constraint on the email field
    email = models.EmailField(('email address'),blank=False,unique=True,help_text='Required',validators=[ValidateEmail])

    def __str__(self):
        return self.username
