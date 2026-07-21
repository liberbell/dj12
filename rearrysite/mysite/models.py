from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Useer must have an email address")
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()