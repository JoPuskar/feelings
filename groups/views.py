from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from django import forms
from .forms import CompanyForm

class CompanyCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CompanyForm
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('groups:dashboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response
