from typing import Any
from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganisorAndLoginRequiredMixin
from .models import Lead
from .forms import LeadModelForm, CustomUserCreationForm


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "webapp/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user

        # Initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(org=user.userprofile)
        else:
            queryset = Lead.objects.filter(org=user.agent.org)
            # Filter the leads of the logged in agent
            queryset = queryset.filter(agent__user=user)

        return queryset


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "webapp/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user

        # Initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(org=user.userprofile)
        else:
            queryset = Lead.objects.filter(org=user.agent.org)
            # Filter the leads of the logged in agent
            queryset = queryset.filter(agent__user=user)

        return queryset


class LeadCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "webapp/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("webapp:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A new lead has been created!",
            message="Go to the dashboard to see the new lead.",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "webapp/lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        # Initial queryset of leads for the entire organisation
        return Lead.objects.filter(org=user.userprofile)

    def get_success_url(self):
        return reverse("webapp:lead-list")


class LeadDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "webapp/lead_delete.html"

    def get_queryset(self):
        user = self.request.user
        # Initial queryset of leads for the entire organisation
        return Lead.objects.filter(org=user.userprofile)

    def get_success_url(self):
        return reverse("webapp:lead-list")
