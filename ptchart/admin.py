from django.contrib import admin
from ptchart.models import Patient, Encounter, ResearchQuestionResponse

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'intake_date')

class EncounterAdmin(admin.ModelAdmin):
    list_display = ('patient', 'id', 'date')

class ResearchQuestionResponseAdmin(admin.ModelAdmin):
    list_display = ('patient', 'encounter', 'research_study', 'research_question', 'response')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Encounter, EncounterAdmin)
admin.site.register(ResearchQuestionResponse, ResearchQuestionResponseAdmin)

