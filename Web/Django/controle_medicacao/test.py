# Importando as classes (models)
from users.models import Usuario, Medicamento, Prescricao, Registro


al1 = Aluno(nome = "Hebert", sobrenome = "Rausch", email = "medicamento@medicamento.org", telefone = "45 99111-0099", senha = "1234")
al2 = Aluno(nome = "Lucas", sobrenome = "Almeida", email = "luc.almeida@pip.com", telefone = "45 90000-0099", senha = "12354")

# salvando cada um dos objetos
al1.save()
al2.save()


#print(user1.nome)


#Criando os medicamentos
# ITEM 2:
medicamentos = [ Medicamento(nome_medicamento = "Doflex", dosagem = "1/dia", forma = "comprimido"), Medicamento(nome_medicamento = "Dipirona", dosagem = "8 gotas/dia", forma = "liquido"), Medicamento(nome_medicamento = "Nesaulgina", dosagem = "2/dia", forma = "comprimido"), Medicamento(nome_medicamento = "Benzetacil", dosagem = "1/mes", forma = "injecao"), Medicamento(nome_medicamento = "Histamin", dosagem = "1/dia", forma = "comprimido") ]


med1 = Medicamento(nome_medicamento = "Doflex", dosagem = "1/dia", forma = "comprimido")
med2 = Medicamento(nome_medicamento = "Dipirona", dosagem = "8 gotas/dia", forma = "liquido")
med3 = Medicamento(nome_medicamento = "Dipirona", dosagem = "8 gotas/dia", forma = "liquido")



#print(medicamento4.nome_medicamento)

#Salvando os medicamentos
for i in range(0, len(medicamentos)):
   medicamentos[i].save()


#Cadastrando Prescrições
#ITEM 3:
prescricoes = []
for user in users:
    for i in range(3):
        prescricoes.append( Prescricao(id_user = user, id_medc = medicamentos[i+1], data_inicio = "2023-01-01", data_fim = "2023-02-15", freq_uso = "Todos os dias") )

for i in range(0, len(prescricoes)):
   prescricoes[i].save()


#Criando Registros   
# ITEM 4 
registros = []   
for prescricao in prescricoes:
    for i in range(2):
        registros.append( Registro(id_presc = prescricao, data_prev = "2023-04-01", hora_prev = "14:00:00", data_toma = "2023-04-15", hora_toma = "15:30:00", obs = "N/A") )

for i in range(0, len(registros)):
   registros[i].save()



#Testando o banco para buscar o id do usuario
#print([user.id_user for user in Usuario.objects.all()])
