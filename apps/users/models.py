from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.template.defaultfilters import slugify
from django_countries.fields import CountryField
phone_regex = RegexValidator(regex=r'^01[0125][0-9]{8}$',
                             message="Phone length is exactly 11, Prefix is with in allowed ones 010, 011, 012, 015")


class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not phone_number:
            raise ValueError("Users must have a phone numbers")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


name_regex = RegexValidator(regex=r'[a-z]', message='This is not a Valid name')


class User(AbstractBaseUser):
    firstname           = models.CharField(max_length=12, validators=[name_regex])
    lastname            = models.CharField(max_length=12, validators=[name_regex])
    username            = models.CharField(max_length=30, unique=True)
    email               = models.EmailField(verbose_name='email')
    phone_number        = models.CharField(max_length=11, validators=[phone_regex])
    country             = models.CharField(max_length=200)
    # address             = models.CharField(max_length=250)

    haveshop           = models.BooleanField(default=False)

    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    hide_information    = models.BooleanField(default=True)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.phone_number

    def has_perm(self, *args, **kwargs):
        return self.is_admin

    def has_module_perms(self, *args, **kwargs):
        return True
