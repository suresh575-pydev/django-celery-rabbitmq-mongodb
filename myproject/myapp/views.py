from rest_framework import viewsets

from .models import Gateway
from .serializers import GatewaySerializer
from .tasks import publish


class GatewayViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer


    def get_queryset(self):
        self.queryset = []

        query_set = Gateway.objects.all()
        for value in query_set:
            payload = dict()

            payload['uid'] = value.uid
            payload['name'] = value.name
            payload['ssid'] = value.ssid
            payload['key'] = value.key
            payload['encryption'] = value.encryption


            publish.delay(payload)

        return query_set


    def perform_create(self, serializer):
        serializer.save()
