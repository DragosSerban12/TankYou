from rest_framework import mixins, viewsets
from .serializers import UsuarioSerializer
from users.models import Usuario
from .paginator import paginador_customizado

class UsuarioViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = UsuarioSerializer
    pagination_class = paginador_customizado
    def get_queryset(self):
        return Usuario.objects.all()


class UsuarioCRUDView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    pagination_class = paginador_customizado
    queryset = Usuario.objects.all()