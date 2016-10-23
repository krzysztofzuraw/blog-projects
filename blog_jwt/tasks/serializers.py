from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
