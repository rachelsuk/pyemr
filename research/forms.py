from django import forms

class NewResearchStudyForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Research Study Name"
        }))

class NewResearchQuestionForm(forms.Form):
    variable = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Data Variable (e.g. 'HR')"
        }))
    text = forms.CharField(widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Research Data Point (e.g. 'heart rate')"
        }))

