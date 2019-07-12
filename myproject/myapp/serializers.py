from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Gateway


class GatewaySerializer(HyperlinkedModelSerializer):


    class Meta:
        model = Gateway
        fields = '__all__'

