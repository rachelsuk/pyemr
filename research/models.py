from django.db import models


class ResearchQuestion(models.Model):
    variable = models.TextField()
    text = models.TextField()
    research_study = models.ForeignKey('ResearchStudy', on_delete=models.CASCADE)
    def __str__(self):
        return self.variable
    class Meta:
        verbose_name_plural = "Research Questions"


class ResearchStudy(models.Model):
    name = models.TextField()
    patient = models.ManyToManyField('ptchart.Patient')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Research Studies"