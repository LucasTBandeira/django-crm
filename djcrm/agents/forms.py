from django import forms
from webapp.models import Agent

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )