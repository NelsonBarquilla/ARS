from django.db import models
from django.db.models.signals import post_save
from web.models import Employee
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(Employee, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=Employee)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Employee)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
