from django.db import models
from django.contrib.auth.models import AbstractUser
from .Usermanager import UserManager
# Create your models here.


class user(AbstractUser):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middel_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=10)

    # imp fields.
    last_login = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50)

    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'middel_name', 'last_name',]

    objects = UserManager()


# This is because the new user class conflicts with Django’s own user class

# error:dmin_app.user.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'Admin_app.user.groups' clashes with reverse accessor for 'auth.User.groups'.
#         HINT: Add or change a related_name argument to the definition for 'Admin_app.user.groups' or 'auth.User.groups'.
# Admin_app.user.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'Admin_app.user.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
#         HINT: Add or change a related_name argument to the definition for 'Admin_app.user.user_permissions' or 'auth.User.user_permissions'.
# auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'Admin_app.user.groups'.
#         HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'Admin_app.user.groups'.
# auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'auth.User.user_permissions' clashes with reverse accessor for 'Admin_app.user.user_permissions'.

# Solutions
# Add a line of configuration in the global setting file and use the custom model class:

# AUTH_USER_MODEL = 'user.User'  #  where user is the app name and User is the model class n
