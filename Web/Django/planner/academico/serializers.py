from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Professor, Curso, Disciplina, ConteudoProgramatico

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # Cria o usuário com o método `create_user` para garantir o hash da senha
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']

class DisciplinaSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)

    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'codigo', 'curso', 'professor']

class DisciplinaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'codigo', 'curso', 'professor']


class ConteudoProgramaticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConteudoProgramatico
        fields = ['descricao']

class DisciplinaConteudoCreateUpdateSerializer(serializers.ModelSerializer):
    conteudos_programaticos = ConteudoProgramaticoSerializer(many=True,  required=False)

    class Meta:
        model = Disciplina
        fields = ['id','curso', 'professor', 'nome', 'codigo', 'conteudos_programaticos']
        read_only_fields = ['id']
        
    def create(self, validated_data):
        conteudos_data = validated_data.pop('conteudos_programaticos', [])
        disciplina = Disciplina.objects.create(**validated_data)
        for conteudo_data in conteudos_data:
            ConteudoProgramatico.objects.create(disciplina=disciplina, **conteudo_data)
        return disciplina
