from rest_framework import serializers
from todoApp.models import Todo, Group
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    group = serializers.ReadOnlyField(source='group.name')

    class Meta:
        model = Todo
        fields = ('owner','id', 'title', 'note', 'completed', 'group')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')