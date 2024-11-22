from django.urls import path
from .views import *

urlpatterns = [
    path('professor/', ProfessorView.as_view()),
    path('professor/<int:pk>/', ProfessorReadUpdateDeleteView.as_view()),

    path('curso/', CursoListCreateAPIView.as_view()),
    
    path('disciplina/', DisciplinaCreateAPIView.as_view()),
    path('disciplinas/', DisciplinaListView.as_view(), name='disciplina-list'),
    path('disciplina/<int:pk>/', DisciplinaRetrieveUpdateDestroyAPIView.as_view()),

    path('disciplina/conteudo', DisciplinaConteudoCreateView.as_view()),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),


]
