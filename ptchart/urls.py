from django.urls import path
from . import views

urlpatterns = [
    path("", views.ptchart_index, name="ptchart_index"),
    path("<int:patient_id>/", views.ptchart_detail, name="ptchart_detail"),
    path("<int:patient_id>/<int:encounter_id>/",
         views.ptchart_encounter, name="ptchart_encounter"),
    path("<int:patient_id>/<int:encounter_id>/<int:research_study_id>/",
         views.ptchart_researchquestionresponse, name="ptchart_researchquestionresponse"),
    path("newpatient/", views.ptchart_newpatient, name="ptchart_newpatient"),
    path("<int:patient_id>/newencounter/",
         views.ptchart_newencounter, name="ptchart_newencounter"),
    path("patientexists/<int:patient_id>",
         views.ptchart_patientexists, name="ptchart_patientexists"),
    path("<int:patient_id>/researchenrollment/",
         views.ptchart_researchenrollment, name="ptchart_researchenrollment"),
    path("<int:patient_id>/alreadyenrolled/<int:research_study_id>/",
         views.ptchart_alreadyenrolled, name="ptchart_alreadyenrolled"),
    path("check-new-pt/", views.check_new_pt, name='check_new_pt'),
]
