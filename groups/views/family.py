from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from braces.views import SetHeadlineMixin

from django import forms
from ..forms import FamilyForm
from ..models import Family


class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = FamilyForm
    headline = 'Create Family'
    template_name = 'families/form.html'
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = FamilyForm
    template_name = 'groups/form.html'
    success_url = reverse_lazy('users:dashboard')

    def get_queryset(self):
        return self.request.user.families.all()

    def get_headline(self):
        return 'Edit {}'.format(self.object.name)


class Detail(LoginRequiredMixin, SetHeadlineMixin, generic.DetailView):
    template_name = 'groups/detail.html'

    def get_queryset(self):
        return self.request.user.families.all()

    def get_headline(self):
        return 'Edit {}'.format(self.object.name)