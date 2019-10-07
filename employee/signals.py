from django.db.models.signals import post_save
from web.models import Employee
from django.dispatch import receiver
from employee.models import Profile


