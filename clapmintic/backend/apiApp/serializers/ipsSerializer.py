from rest_framework import serializers
from apiApp.models.ips import Ips

class IpsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ips 
        fields=('id_reps','nombre','tipo_de_entidad','representante','nivel_de_atencion')