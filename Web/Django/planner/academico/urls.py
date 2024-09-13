from django.urls import path
from .views import ProfessorView, ProfessorReadUpdateDeleteView, CursoListCreateAPIView, DisciplinaListCreateAPIView, DisciplinaRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('professor/', ProfessorView.as_view()),
    path('professor/<int:pk>/', ProfessorReadUpdateDeleteView.as_view()),

    path('curso/', CursoListCreateAPIView.as_view()),
    
    path('disciplina/', DisciplinaListCreateAPIView.as_view()),
    path('disciplina/<int:pk>/', DisciplinaRetrieveUpdateDestroyAPIView.as_view()),

]
