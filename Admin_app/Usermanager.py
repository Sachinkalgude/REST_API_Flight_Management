from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.is_verify = False
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not password:
            raise ValueError("password should not be none")

        # For Saving Method
        user = self.create_user(email, password)

        user.is_active = True
        user.is_verify = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
