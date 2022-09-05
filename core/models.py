import uuid

"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the systems."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Category(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    # restaurantId =
    categoryName = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    # lastUpdate =


class TableManagement(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    # restaurantId =
    tableName = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    # lastUpdate =


class Restaurants(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    # userId =
    address = models.TextField(max_length=255)
    cellPhone = PhoneNumberField()
    emial = models.EmailField(max_length=254)
    profile = models.ImageField(null=True, blank=True, default="default.jpg")
    restaurantName = models.CharField(max_length=25)
    social = models.CharField(max_length=25)
    website = models.CharField(max_length=50)
    isDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    # lastUpdate =
