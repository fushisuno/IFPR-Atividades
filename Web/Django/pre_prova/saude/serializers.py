from rest_framework import serializers
from .models import Usuario, Medicamento, Prescricao

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ['nome_medicamento', 'dosagem', 'forma']

#Serializer para realizar as operações em apenas 1 prescrição
class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescricao
        fields = '__all__'

#Serializer Para Recuperar as Prescricões e Medicamentos
class PrescricaoMedicamentoRetrieveSerializer(serializers.ModelSerializer):
    medicamentos = MedicamentoSerializer(many=True, read_only=True)

    class Meta:
        model = Prescricao
        fields = ['id_presc', 'id_user', 'data_inicio', 'data_fim', 'freq_uso', 'medicamentos']

#Serializer Para Criar as Prescricões e Medicamentos de forma simultanea
class PrescricaoMedicamentoCreateUpdateSerializer(serializers.ModelSerializer):
    medicamentos = MedicamentoSerializer(many=True)

    class Meta:
        model = Prescricao
        fields = ['id_presc', 'id_user', 'data_inicio', 'data_fim', 'freq_uso', 'medicamentos']
        read_only_fields = ['id_presc']

    def create(self, validated_data):
        medicamentos_data = validated_data.pop('medicamentos')
        prescricao = Prescricao.objects.create(**validated_data)
        for medicamento_data in medicamentos_data:
            Medicamento.objects.create(prescricao=prescricao, **medicamento_data)
        return prescricao