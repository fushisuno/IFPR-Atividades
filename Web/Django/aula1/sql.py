import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aula1.settings")

import django
django.setup()

from django.core.management import call_command


from alunos.models import Aluno, Disciplina, Curso, Professor

'''
 Insira 3 alunos no banco de dados
'''

# criando os objetos
al1 = Aluno(nome="Felipe", data_nascimento="2000-10-21")
al2 = Aluno(nome="Rausch",  data_nascimento="2000-10-21")
al3 = Aluno(nome="Fernandes",  data_nascimento="2000-10-21")

# salvando cada um dos objetos
al1.save()
al2.save()
al3.save()

'''
Insira dois cursos
'''

c1 = Curso(nome="TADS")
c1.save()
c2 = Curso(nome="Ciencia")
c2.save()


'''
Para cada curso, insira 3 disciplinas no banco de dados.
'''
disciplina = Disciplina(nome="Banco de dados I", codigo="BD1", curso=c1)
disciplina.save()
disciplina = Disciplina(nome="Banco de dados II", codigo="BD2", curso=c1)
disciplina.save()
disciplina = Disciplina(nome="Desenvolvimento Web 2", codigo="WEB", curso=c1)
disciplina.save()

disciplina = Disciplina(nome="Compiladores", codigo="COMP", curso=c2)
disciplina.save()
disciplina = Disciplina(nome="Organizacao", codigo="AO", curso=c2)
disciplina.save()
disciplina = Disciplina(nome="Automatos I", codigo="AUT1", curso=c2)
disciplina.save()

c3 = Curso(nome="Matematica")
d1c3 = Disciplina(nome="Calculo", codigo="CAL", curso=c3)
d1c3.save()
c3.save()
d1c3.save()

'''
CONSULTAS
'''

#Liste o nome de todos os alunos salvos no banco de dados.
'''lista_alunos = Aluno.objects.all()
for item in lista_alunos:
    print(item.nome)'''

print([aluno.nome for aluno in Aluno.objects.all()])

#Para cada curso, liste o nome das disciplinas associadas a ele.
lista_cursos = Curso.objects.all()
for item_curso in lista_cursos:
    lista_disciplinas = item_curso.disciplina_set.all()
    print(lista_disciplinas)

#Liste o nome do curso relacionado à disciplina que tem a chave primária igual a 2.
disc2 = Disciplina.objects.get(pk=2)
print(disc2.curso.nome)
print(disc2.curso)

#Procure pelas disciplinas que tem o nome igual a “WEB”
# - Procure identicamente;f
disc2 = Disciplina.objects.get(codigo="WEB2")
disc2 = Disciplina.objects.filter(codigo="WEB2")

# - Procure desconsiderando o maiúsculo/minúsculo
disc2 = Disciplina.objects.get(codigo="web2")
disc2
disc2 = Disciplina.objects.get(codigo__iexact="web2")
disc2

#liste as disciplinas do curso de TADS
lista_disc_tads = Disciplina.objects.filter(curso__nome="TADS")

'''
ALTERANDO O BANCO DE DADOS
'''

#Crie uma nova entidade Professor com atributo nome;
#Um professor pode lecionar várias disciplinas (faça o ajuste necessário para atender este requisito);
#Faça a migração do banco de dados.
#Adicione 3 professores, um deles chamado “Ciclano”.
professor = Professor(nome="Ciclano")
professor.save()

professor = Professor(nome="Beltrano")
professor.save()

professor = Professor(nome="Fulano")
professor.save()

#Atribua o professor “Ciclano” à todas as disciplinas do curso “TADS”.
ciclano = Professor.objects.get(nome="Ciclano")
lista_disc_tads = Disciplina.objects.filter(curso__nome="TADS")

for disciplina in lista_disc_tads:
    disciplina.professor = ciclano
    disciplina.save()
