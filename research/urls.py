from django.urls import path
from . import views

urlpatterns = [
    path("", views.research_index, name="research_index"),
    path("<int:research_id>/", views.research_detail, name="research_detail"),
    path("newstudy/", views.research_newstudy, name="research_newstudy"),
    path("<int:research_id>/newquestion/", views.research_newquestion, name="research_newquestion"),
]