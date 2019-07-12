class GatewayViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer



    '''
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        data = self.get_object()
        return Response(data.highlighted)
    '''
    def perform_create(self, serializer):
        serializer.save()
    '''
    def retrieve(self,):
        if id==None:
            queryset = Gateway.objects.all()
            publish.delay(queryset)
        else:
            queryset = Gateway.objects.all().get(id=id)
            publish.delay(queryset)
    '''