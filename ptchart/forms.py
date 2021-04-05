from django import forms
from django.db import models
from ptchart.models import ResearchQuestionResponse
from research.models import ResearchStudy


class NewPatientForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Patient Name (e.g. 'Donald Duck')"
        }))
    dob = forms.DateField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Birthdate (mm/dd/yyyy)"
        }))
    race = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Patient Race"
        }))
    intake_date = forms.DateField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Intake Date (mm/dd/yyyy)"
        }))


class NewEncounterForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Date of Encounter (mm/dd/yyyy)"
        }))
    body = forms.CharField(widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Encounter Notes"
        }))    
        

class ResearchQuestionResponseForm(forms.Form):
    response =  forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
        }))


class ResearchEnrollmentForm(forms.Form):
    research_study = forms.ModelChoiceField(ResearchStudy.objects.all())