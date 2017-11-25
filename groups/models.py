import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField


class Group(models.Model):
    created_at = models.DateTimeField(default=timezone.now())
    created_by = models.ForeignKey(User, related_name='%(class)s_created')
    name = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Family(Group):
    members = models.ManyToManyField(User, related_name='families')

    class Meta:
        verbose_name_plural = 'families'


class Company(Group):
    members = models.ManyToManyField(User, related_name='companies')

    class Meta:
        verbose_name_plural = 'companies'

INVITE_STATUSES = (
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Rejected')
)

class Invite(models.Model):
    from_user = models.ForeignKey(User, related_name='%(class)s_created')
    to_user = models.ForeignKey(User, related_name='%(class)s_received')
    status = models.IntegerField(default=0, choices=INVITE_STATUSES)
    uuid = models.CharField(max_length=32, default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{} invited by {}'.format(self.to_user, self.from_user)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.uuid = uuid.uuid4().hex
        super().save(*args, **kwargs)


class CompanyInvite(Invite):
    company = models.ForeignKey(Company, related_name='invites')

    def __str__(self):
        return '{} invited to {} by {}'.format(self.to_user, self.company, self.from_user)


class FamilyInvite(Invite):
    family = models.ForeignKey(Family, related_name='invites')

    def __str__(self):
        return '{} invited to {} by {}'.format(self.to_user, self.family, self.from_user)



