from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404

#importando modelos e serializers
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny 

class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny] # Permite acesso público a este endpoint
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            ''' Usado para criar um user e ja loga-lo no sistema
            # Cria o token para o novo usuário
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            '''
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorView(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfessorReadUpdateDeleteView(APIView):
    """
    View para recuperar, atualizar ou deletar um professor específico.
    """

    def get(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)

        '''
        try:
            professor = Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            return Response({'detail': 'Professor não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        '''

        serializer = ProfessorSerializer(professor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CursoListCreateAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaFilter(filters.FilterSet):
    curso = filters.CharFilter(field_name="curso__nome", lookup_expr='icontains')
    professor = filters.CharFilter(field_name="professor__nome", lookup_expr='icontains')
    conteudos_programaticos = filters.CharFilter(
        field_name="conteudos_programaticos__descricao", lookup_expr='icontains'
    )
    nome = filters.CharFilter(field_name="nome", lookup_expr='icontains')

    class Meta:
        model = Disciplina
        fields = ['curso', 'professor', 'conteudos_programaticos', 'nome']

class DisciplinaListView(generics.ListAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DisciplinaFilter


class DisciplinaCreateAPIView(APIView):

    def post(self, request):
        serializer = DisciplinaCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplinaCreateUpdateSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DisciplinaConteudoCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DisciplinaConteudoCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

