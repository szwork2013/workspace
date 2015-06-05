from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    user = models.OneToOneField(User, editable=False, related_name='profile')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username


class ProfilePhoto(models.Model):

    profile = models.ForeignKey(Profile, related_name='photos')
    title = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return self.title or 'noname'

    def get_absolute_url(self):
        return self.image.url if self.image else ''


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)


models.signals.post_save.connect(create_profile, sender=User)
