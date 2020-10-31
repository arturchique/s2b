from django.shortcuts import render
from django.views.decorators.http import require_GET
from openpyxl import load_workbook
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser


class AdminView(APIView):
    def post(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        shelter = worker.shelter
        if worker.position == "w":
            if not request.data["filters"]:
                animals = Animal.objects.filter(shelter=shelter,
                                                animal_accounting_card__contains=request.data["search"])
                paginator = Paginator(animals, 15)
                page = request.data["page"]
                paged_listings = paginator.get_page(page)
                serializer = AnimalSerializer(paged_listings, many=True)
                return Response({
                    "data": serializer.data,
                    "status": "w",
                    "total_page_count": paginator.num_pages
                })
            else:
                pass
        elif worker.position == "a":
            return Response({"data": "Это админ приюта"})
        return Response({"data": "ok"})


class AdminAddView(APIView):
    def post(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        shelter = worker.shelter
        data = request.data

        new_animal = Animal(animal_accounting_card=data["animal_accounting_card"], kind=data["kind"],
                            birth_date=data["birth_date"], weight=data["weight"], shelter=shelter,
                            name=data["name"], sex=data["sex"], breed=data["breed"], cage_number=data["cage_number"],
                            color=data["color"], hair=data["hair"], ears=data["ears"], tail=data["tail"],
                            size=data["size"], identifying_marks=data["identifying_marks"],
                            animal_id=data["animal_id"], sterilization_date=data["sterilization_date"],
                            doctor_name=data["doctor_name"], socialized=data["socialized"], region=data["region"],
                            catching_act_order=data["catching_act_order"], catching_act_date=data["catching_act_date"],
                            catching_act=data["catching_act"], catching_address=data["catching_address"],
                            legal_entity=data["legal_entity"], owner_name=data["owner_name"],
                            person_owner_name=data["person_owner_name"], entrance_act_date=data["entrance_act_date"],
                            entrance_act=data["entrance_act"], leaving_act_date=data["leaving_act_date"],
                            leaving_act_reason=data["leaving_act_reason"], leaving_act=data["leaving_act"],
                            staff_name=data["staff_name"], parasites_treatment=data["parasites_treatment"],
                            vaccinations=data["vaccinations"], medical_checkup_date=data["medical_checkup_date"],
                            anamnesis=data["anamnesis"],
                            )
