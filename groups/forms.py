from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q

from . import models


class FamilyForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'description')
        model = models.Family


class CompanyForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'description')
        model = models.Company


class CompanyInviteForm(forms.Form):
    email_or_username = forms.CharField(label="Email or Username")

    def clean_email_or_username(self):
        data = self.cleaned_data['email_or_username']
        try:

            self.invitee = models.User.objects.get(
                Q(email=data)|Q(username=data)
            )
        except models.User.DoesNotExist:
            raise ValidationError('No such user')

        return data
