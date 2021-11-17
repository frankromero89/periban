from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """Profile Model"""
    OPERATOR = 'Optor'
    ADMIN = 'Admin'
    ROLES = [
        (ADMIN, 'Administrador'),
        (OPERATOR, 'Operador'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=5,
        choices=ROLES,
        default=OPERATOR
    )
