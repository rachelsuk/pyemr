from django.shortcuts import render
from research.models import ResearchStudy, ResearchQuestion
from research.forms import NewResearchStudyForm, NewResearchQuestionForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def research_index(request):
    research_studies = ResearchStudy.objects.all()
    context = {"research_studies": research_studies}
    return render(request, 'research_index.html', context)

def research_detail(request, research_id):
    research_study = ResearchStudy.objects.get(id=research_id)
    research_questions = ResearchQuestion.objects.filter(research_study__id=research_id)
    context = {"research_study": research_study, "research_questions": research_questions}
    return render(request, 'research_detail.html', context)

def research_newstudy(request):
    form = NewResearchStudyForm()
    if request.method == 'POST':
        form = NewResearchStudyForm(request.POST)
        if form.is_valid():
            research_study = ResearchStudy(
                name=form.cleaned_data["name"],
            )
            research_study.save()
            return HttpResponseRedirect(reverse('research_detail', args=(research_study.id,)))
    context = {"form": form}
    return render(request, "research_newstudy.html", context)

def research_newquestion(request, research_id):
    form = NewResearchQuestionForm()
    research_study = ResearchStudy.objects.get(id=research_id)
    if request.method == 'POST':
        form = NewResearchQuestionForm(request.POST)
        if form.is_valid():
            research_question = ResearchQuestion(
                variable=form.cleaned_data["variable"],
                text=form.cleaned_data["text"],
                research_study=research_study
            )
            research_question.save()
            return HttpResponseRedirect(reverse('research_detail', args=(research_study.id,)))
    context = {"form": form, "research_study": research_study}
    return render(request, "research_newquestion.html", context)