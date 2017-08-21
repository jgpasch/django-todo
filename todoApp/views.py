from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from todoApp.serializers import UserSerializer, RegistrationSerializer, TodoSerializer, GroupSerializer
from todoApp.models import Todo, Group

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, TokenHasScope,)
    queryset = User.objects.all()
    required_scopes = ['read', 'write']
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, TokenHasScope,)
    queryset = Group.objects.all()
    required_scopes = ['read', 'write']
    serializer_class = GroupSerializer

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, TokenHasScope,)
    queryset = Todo.objects.all()
    required_scopes = ['read', 'write']
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_create(self, serializer):
        gr = Group.objects.get(name=self.request.data['group'])
        serializer.save(owner=self.request.user, group=gr)
