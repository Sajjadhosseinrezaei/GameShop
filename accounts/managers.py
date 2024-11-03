from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):

    def create_user(self, name, family, email, password=None):
        if not email:
            raise ValueError("User must be an email address")

        user = self.model(name=name, family=family, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, family, email, password=None):
        user = self.create_user(name, family, email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
