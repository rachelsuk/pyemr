from django.db import models
from django.forms import ModelForm


class Patient(models.Model):
    name = models.TextField()
    dob = models.DateField()
    race = models.TextField()
    intake_date = models.DateField()
    def __str__(self):
        return self.name


class Encounter(models.Model):
    date = models.DateField()
    body = models.TextField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.date)


class ResearchQuestionResponse(models.Model):
    response = models.TextField()
    research_question = models.ForeignKey('research.ResearchQuestion', on_delete=models.CASCADE)
    research_study = models.ForeignKey('research.ResearchStudy', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    encounter = models.ForeignKey('Encounter', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "Research Question Responses"


