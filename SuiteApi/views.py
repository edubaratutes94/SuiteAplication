from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from SuiteApi.serializers import *
from django.contrib.auth import login as django_login
from SuiteApp.utils import *
from SuiteApi.serializers import *
from SuiteApp.models import *

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        register_logs(request, UserApp, "", user.__str__(), 10)
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"key": token.key, "userid": user.id}, status=200)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# NOMENCLADORES Listado----------------------------------------------------------------------------

class TipoViviendaList(viewsets.ModelViewSet):
    serializer_class = TipoViviendaSerializer
    permission_classes = [IsAuthenticated]
    authorization_classes = [TokenAuthentication]

    def get_queryset(self):
        return Tipo_vivienda.objects.all()

class TipoAlojamientoList(viewsets.ModelViewSet):
    serializer_class = TipoAlojamientoSerializer
    permission_classes = [IsAuthenticated]
    authorization_classes = [TokenAuthentication]

    def get_queryset(self):
        return Tipo_alojamiento.objects.all()

class TipoCamaList(viewsets.ModelViewSet):
    serializer_class = TipoViviendaSerializer
    permission_classes = [IsAuthenticated]
    authorization_classes = [TokenAuthentication]

    def get_queryset(self):
        return Tipo_cama.objects.all()

# CRUD REGISTRO VIVIENDA----------------------------------------------------------------------------

class RegistroViviendaCreate(generics.CreateAPIView):
    queryset = Registrovivienda.objects.all()
    serializer_class = RegistroViviendaSerializer

class RegistroViviendaList(generics.ListAPIView):
    queryset = Registrovivienda.objects.all()
    serializer_class = RegistroViviendaSerializer

class RegistroViviendaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Registrovivienda.objects.all()
    serializer_class = RegistroViviendaSerializer

class RegistroViviendaDelete(generics.DestroyAPIView):
    queryset = Registrovivienda.objects.all()
    serializer_class = RegistroViviendaSerializer

