from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from datetime import date

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


class Form_type(models.Model):
    """Questions Forms Model"""
    form_id = models.AutoField(primary_key=True)
    form_name = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)
    total_points_promedy = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.form_name


class Question_form(models.Model):
    """Questions Forms Model"""
    question_id = models.AutoField(primary_key=True)
    question_description = models.CharField(max_length=700, default="")
    form_type = models.ForeignKey(Form_type, on_delete=models.CASCADE)
    is_options = models.BooleanField(default=False)
    is_check = models.BooleanField(default=False)
    is_time = models.BooleanField(default=False)
    is_picture = models.BooleanField(default=False)
    value_points = models.IntegerField(default=0, blank=False, null=False)
    options = models.TextField(blank=True, null=True)
    required = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(default= timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_description
    
    class Meta(object):
        ordering = ['my_order']

class answer_form(models.Model):
    form_id = models.IntegerField()
    form_type = models.ForeignKey(Form_type, on_delete=models.CASCADE, default="1")
    question_id = models.ForeignKey(Question_form, on_delete=models.CASCADE)
    answer = models.TextField(default="")
    answer_by = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    created = models.DateField(default= date.today)

    def __str__(self):
        return self.answer

class image_evidence(models.Model):
    id = models.AutoField(primary_key=True)
    form_id = models.IntegerField(default=1)
    image_evidence = models.ImageField(upload_to='landing/images/evidence', null=True)
    created = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ('-id',)

class promedy_form(models.Model):
    form_id = models.IntegerField()
    promedy_form = models.PositiveIntegerField(default=0, blank=False, null=False)
    created = models.DateField(default= date.today)
    def __str__(self):
        return self.promedy_form

