from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.views import generic

from braces.views import SetHeadlineMixin

from .. import models
from .. import forms


class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = forms.FamilyForm
    headline = 'Create Family'
    template_name = 'families/form.html'
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = forms.FamilyForm
    template_name = 'families/form.html'

    def get_queryset(self):
        return self.request.user.families.all()

    def get_headline(self):
        return 'Edit {}'.format(self.object.name)

    def get_success_url(self):
        return reverse('groups:families:detail', kwargs={'slug': self.object.slug})


class Detail(LoginRequiredMixin, generic.FormView):
    template_name = 'families/detail.html'
    form_class = forms.FamilyInviteForm

    def get_success_url(self):
        self.get_object()
        return reverse('groups:families:detail', kwargs={'slug': self.object.slug})

    def get_queryset(self):
        return self.request.user.families.all()

    def get_object(self):
        self.object = self.request.user.families.get(
            slug=self.kwargs.get('slug')
        )
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        models.FamilyInvite.objects.create(
            from_user=self.request.user,
            to_user=form.invitee,
            family=self.get_object()
        )
        return response


class Invites(LoginRequiredMixin, generic.ListView):
    template_name = 'families/invites.html'

    def get_queryset(self):
        return self.request.user.familyinvite_received.filter(status=0)


class InviteResponse(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy('groups:families:invites')

    def get(self, request, *args, **kwargs):
        invite = get_object_or_404(
            models.FamilyInvite,
            to_user=request.user,
            uuid=kwargs.get('code'),
            status=0
        )
        if kwargs.get('response') == 'accept':
            invite.status = 1
        else:
            invite.status = 2

        invite.save()

        return super().get(request, *args, **kwargs)