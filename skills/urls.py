from django.urls import path
from .views import SkillListCreateView

urlpatterns = [
    path("skills/", SkillListCreateView.as_view(), name="skill-list"),
]
