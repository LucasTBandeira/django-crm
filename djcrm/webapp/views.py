from django.views import generic
from django.urls import reverse
from .models import Lead
from .forms import LeadModelForm


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = "webapp/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    template_name = "webapp/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    template_name = "webapp/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("webapp:lead-list")


class LeadUpdateView(generic.UpdateView):
    template_name = "webapp/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("webapp:lead-list")


class LeadDeleteView(generic.DeleteView):
    template_name = "webapp/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("webapp:lead-list")
