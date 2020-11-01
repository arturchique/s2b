from rest_framework import serializers
from .models import *


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"


class AdminAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ("sex", "birth_date", "color", "hair",
                  "vaccinations", "sterilization_date", "breed")


