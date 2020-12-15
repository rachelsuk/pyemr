from django.contrib import admin
from research.models import ResearchStudy, ResearchQuestion

class ResearchStudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ResearchQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'variable')


admin.site.register(ResearchStudy, ResearchStudyAdmin)
admin.site.register(ResearchQuestion, ResearchQuestionAdmin)