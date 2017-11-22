from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic

from braces.views import SetHeadlineMixin

from ..forms import FamilyForm


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
    template_name = 'families/form.html'

    def get_queryset(self):
        return self.request.user.families.all()

    def get_headline(self):
        return 'Edit {}'.format(self.object.name)

    def get_success_url(self):
        return reverse('groups:families:detail', kwargs={'slug': self.object.slug})


class Detail(LoginRequiredMixin, generic.DetailView):
    template_name = 'families/detail.html'

    def get_queryset(self):
        return self.request.user.families.all()