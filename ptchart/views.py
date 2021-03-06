from django.shortcuts import render
from ptchart.models import Patient, Encounter, ResearchQuestionResponse
from research.models import ResearchQuestion, ResearchStudy
from ptchart.forms import NewPatientForm, NewEncounterForm, ResearchQuestionResponseForm, ResearchEnrollmentForm
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse


def ptchart_index(request):
    patients = Patient.objects.all().order_by('name')
    # searched_pt = request.GET.get('name')
    # print(searched_pt)
    # if searched_pt:
    #     patients = Patient.objects.filter(
    #         name=searched_pt).order_by('name')
    context = {
        'patients': patients,
    }
    return render(request, 'ptchart_index.html', context)


def ptchart_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    encounters = Encounter.objects.filter(
        patient__id=patient_id).order_by('-date')
    research_study = ""
    if ResearchStudy.objects.filter(patient__id=patient_id).exists():
        research_study = ResearchStudy.objects.get(patient__id=patient_id)
    context = {
        'patient': patient,
        'encounters': encounters,
        'research_study': research_study,
    }
    return render(request, 'ptchart_detail.html', context)


def ptchart_encounter(request, patient_id, encounter_id):
    patient = Patient.objects.get(id=patient_id)
    encounter = Encounter.objects.get(id=encounter_id)
    research_study = ""
    qa_pairs = ""
    if ResearchStudy.objects.filter(patient__id=patient_id).exists():
        research_study = ResearchStudy.objects.get(patient__id=patient_id)
        research_questions = ResearchQuestion.objects.filter(
            research_study__id=research_study.id)
        research_questionresponses = ResearchQuestionResponse.objects.filter(
            patient__id=patient_id, encounter__id=encounter_id, research_study__id=research_study.id)
        qa_pairs = zip(research_questions, research_questionresponses)
    context = {
        'encounter': encounter,
        'patient': patient,
        'research_study': research_study,
        'qa_pairs': qa_pairs,
    }
    return render(request, 'ptchart_encounter.html', context)


def ptchart_newpatient(request):
    form = NewPatientForm()
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            patient = Patient(
                intake_date=form.cleaned_data["intake_date"],
                name=form.cleaned_data["name"],
                dob=form.cleaned_data["dob"],
                race=form.cleaned_data["race"],
            )
            # if Patient.objects.filter(name=patient.name, dob=patient.dob).exists():
            #     existing_patient = Patient.objects.get(
            #         name=patient.name, dob=patient.dob)
            #     return HttpResponseRedirect(reverse('ptchart_patientexists', args=(existing_patient.id,)))
            # else:
            patient.save()
            return HttpResponseRedirect(reverse('ptchart_detail', args=(patient.id,)))
    context = {"form": form}
    return render(request, "ptchart_newpatient.html", context)


def check_new_pt(request):
    form = NewPatientForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        dob = form.cleaned_data["dob"]
        if Patient.objects.filter(name=name, dob=dob).exists():
            existing_patient = Patient.objects.get(
                name=name, dob=dob)
            print("this works")
            return existing_patient.id


def ptchart_newencounter(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    research_study = ResearchStudy.objects.filter(patient__id=patient_id)

    form = NewEncounterForm()
    if request.method == 'POST':
        form = NewEncounterForm(request.POST)
        if form.is_valid():
            encounter = Encounter(
                date=form.cleaned_data["date"],
                body=form.cleaned_data["body"],
                patient=patient
            )
            encounter.save()
            if research_study.exists():
                research_study = ResearchStudy.objects.get(
                    patient__id=patient_id)
                return HttpResponseRedirect(reverse('ptchart_researchquestionresponse', args=(patient.id, encounter.id, research_study.id,)))
            else:
                return HttpResponseRedirect(reverse('ptchart_detail', args=(patient.id,)))
    context = {"form": form, "patient": patient}
    return render(request, "ptchart_newencounter.html", context)


def ptchart_patientexists(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    context = {"patient": patient}
    return render(request, "ptchart_patientexists.html", context)


def ptchart_researchquestionresponse(request, patient_id, encounter_id, research_study_id):
    patient = Patient.objects.get(id=patient_id)
    encounter = Encounter.objects.get(id=encounter_id)
    research_study = ResearchStudy.objects.get(patient__id=patient_id)
    research_questions = ResearchQuestion.objects.filter(
        research_study__id=research_study_id)
    form = ResearchQuestionResponseForm()
    if request.method == 'POST':
        form = ResearchQuestionResponseForm(request.POST)
        if form.is_valid():
            responses = request.POST.getlist('response')
            i = 0
            for research_question in research_questions:
                research_questionresponse = ResearchQuestionResponse(
                    response=responses[i],
                    research_question=research_question,
                    research_study=research_study,
                    patient=patient,
                    encounter=encounter,
                )
                research_questionresponse.save()
                i += 1
            return HttpResponseRedirect(reverse('ptchart_detail', args=(patient.id,)))
    context = {"form": form, "patient": patient, "encounter": encounter,
               "research_questions": research_questions, "research_study": research_study}
    return render(request, "ptchart_researchquestionresponse.html", context)


def ptchart_researchenrollment(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    form = ResearchEnrollmentForm()
    if request.method == 'POST':
        form = ResearchEnrollmentForm(request.POST)
        if form.is_valid():
            if ResearchStudy.objects.filter(patient=patient).exists():
                enrolled_study = ResearchStudy.objects.get(patient=patient)
                return HttpResponseRedirect(reverse('ptchart_alreadyenrolled', args=(patient.id, enrolled_study.id)))
            else:
                research_study = form.cleaned_data['research_study']
                research_study.patient.add(patient)
                return HttpResponseRedirect(reverse('ptchart_detail', args=(patient.id,)))
    context = {"form": form, "patient": patient}
    return render(request, "ptchart_researchenrollment.html", context)


def ptchart_alreadyenrolled(request, patient_id, research_study_id):
    patient = Patient.objects.get(id=patient_id)
    research_study = ResearchStudy.objects.get(id=research_study_id)
    context = {"patient": patient, "research_study": research_study}
    return render(request, "ptchart_alreadyenrolled.html", context)
