from django.urls import reverse
from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.text import slugify
from uuid import uuid4
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


class Product(models.Model):
    id = models.UUIDField(default=uuid4(),unique=True,primary_key=True)
    name = models.CharField(max_length=614)
    slug = models.SlugField(blank=True,max_length=124)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    def get_absolute_url(self):
        #product_detail is the view
        return reverse("accounts:product_detail", args=[
            self.id,
            self.slug
        ])
    

    def __str__(self):
        return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    username = models.CharField(max_length=614)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.username} on {self.product}'

class Platform(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    purchase_page = models.URLField()
    product = models.ForeignKey(Product,on_delete=models.PROTECT,related_name='platforms')

