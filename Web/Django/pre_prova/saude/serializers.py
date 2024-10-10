from rest_framework import serializers
from .models import Usuario, Medicamento, Prescricao

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields = '__all__'

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Medicamento
        fields = '__all__'

class PrescricaoMedicamentoCreateUpdateSerializer(serializers.ModelSerializer):
    medicamentos = MedicamentoSerializer(many=True, required=False)

    class Meta:
        model = Prescricao
        fields = '__all__'

    def create(self, validated_data):
        medicamentos_data = validated_data.pop('medicamentos', [])
        prescricao = Prescricao.objects.create(**validated_data)
        for medicamento_data in medicamentos_data:
            Medicamento.objects.create(prescricao=prescricao, **medicamento_data)
        return prescricao