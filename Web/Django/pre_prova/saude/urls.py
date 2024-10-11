from django.urls import path
from .views import *

urlpatterns = [
  #Criando as rotas de cada pagina vista pelo usuario
  path('usuario', UsuarioView.as_view()),
  path('usuario/<int:pk>/', UsuarioReadUpdateDeleteView.as_view(), name='usuario-detail'),
  path('prescricao/<int:pk>/', PrescricaoReadUpdateDeleteView.as_view()),
  path('prescricao/medicamento', PrescricaoMedicamentoCreateUpdateView.as_view()),
]