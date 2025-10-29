from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .models import Endereco
from .serializers import EnderecoSerializer
from .servicos import consulta_viacep
# Create your views here.
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [permissions.AllowAny]

    def consultar (self, request, cep=None):
        cep = request.data.get("cep")
        try:
            dados = consulta_viacep(cep)
            obj = Endereco.objects.update_or_create(cep = dados["cep"], defaults=dados)
            serializer = self.get_serializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"erro": str(e)}, status=status.HTTP_404_NOT_FOUND)

   