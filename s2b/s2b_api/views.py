from django.shortcuts import render
from django.views.decorators.http import require_GET
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from .glossary import *
from .reports import docx_export


class AdminView(APIView):
    def get(self, request):
        user = request.user
        animal_accounting_card = request.GET.get("animal_accounting_card", "---------")
        worker = Worker.objects.get(user=user)
        shelter = worker.shelter
        try:
            animal = Animal.objects.get(animal_accounting_card=animal_accounting_card, shelter=shelter)
            serializer = AnimalSerializer(animal)
            return Response({"data": serializer.data})
        except:
            return Response({"data": "Такого животного не существует"})

    def post(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        shelter = worker.shelter
        if worker.position == "w" or worker.position == "a" or worker.position == "d":
            if not request.data["filters"]:
                animals = Animal.objects.filter(shelter=shelter,
                                                animal_accounting_card__contains=request.data["search"])
                paginator = Paginator(animals, 15)
                page = request.data["page"]
                paged_listings = paginator.get_page(page)
                serializer = AnimalSerializer(paged_listings, many=True)
                return Response({
                    "data": serializer.data,
                    "status": f"{worker.position}",
                    "total_page_count": paginator.num_pages
                })
            else:
                pass
        elif worker.position == "a":
            return Response({"status": ""})
        return Response({"data": "ok"})


class AdminAddView(APIView):
    def get(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        if worker.position == "w" or worker.position == "a":
            return Response({
                "animal_accounting_card": {"values": "string", "*": 1, "text": "Номер карточки учета животного"},
                "kind": {"values": [kind[0] for kind in ANIMAL_KIND_CHOICES], "*": 1, "text": "Вид животного"},
                "birth_date": {"values": "string", "*": 1, "text": "Возраст, дата рождения"},
                "weight": {"values": "float", "*": 1, "text": "Вес"},
                "name": {"values": "string", "*": 0, "text": "Кличка"},
                "sex": {"values": ["Мужской", "Женский"], "*": 1, "text": "Пол"},
                "breed": {"values": [breed[0] for breed in ANIMAL_BREED_CHOICES], "*": 1, "text": "Порода"},
                "cage_number": {"values": "int", "*": 1, "text": "Номер вольера"},
                "color": {"values": [color[0] for color in ANIMAL_COLOR_CHOICES], "*": 1, "text": "Окрас"},
                "hair": {"values": [hair[0] for hair in ANIMAL_HAIR_CHOICES], "*": 1, "text": "Шерсть"},
                "ears": {"values": [ears[0] for ears in ANIMAL_EAR_CHOICES], "*": 1, "text": "Уши"},
                "tail": {"values": [tail[0] for tail in ANIMAL_TAIL_CHOICES], "*": 1, "text": "Хвост"},
                "size": {"values": ["Маленький", "Средний", "Большой"], "*": 1, "text": "Размер"},
                "identifying_marks": {"values": "string", "*": 1, "text": "Особые приметы ('нет', если нет)"},
                "animal_id": {"values": "string", "*": 1, "text": "Идентификационная метка"},
                "sterilization_date": {"values": "string", "*": 1, "text": "Дата стерилизации"},
                "doctor_name": {"values": "string", "*": 1, "text": "ФИО вет. врача"},
                "socialized": {"values": "bool", "*": 1, "text": "Готово к социализации"},
                "region": {"values": "string", "*": 1, "text": "Административный округ"},
                "catching_act_order": {"values": "string", "*": 1, "text": "Заказ-наряд / акт о поступлении животного №"},
                "catching_act_date": {"values": "string", "*": 1, "text": "Заказ-наряд / акт о поступлении животного, дата"},
                "catching_act": {"values": "string", "*": 1, "text": "Акт отлова"},
                "catching_address": {"values": "string", "*": 1, "text": "Адрес места отлова"},
                "legal_entity": {"values": "string", "*": 0, "text": "Юр. Лицо"},
                "owner_name": {"values": "string", "*": 0, "text": "ФИО опекунов"},
                "person_owner_name": {"values": "string", "*": 0, "text": "Физическое лицо ФИО"},
                "entrance_act_date": {"values": "string", "*": 1, "text": "Дата поступления в приют"},
                "entrance_act": {"values": "string", "*": 1, "text": "Акт поступления в приют"},
                "leaving_act_date": {"values": "string", "*": 0, "text": "Дата выбытия из приюта"},
                "leaving_act_reason": {"values": [reason[0] for reason in LEAVING_REASON_CHOICES],
                                       "*": 0,
                                       "text": "Причина выбытия из приюта"},
                "staff_name": {"values": "string", "*": 0, "text": "ФИО сотрудника по уходу за животным"},
                "parasites_treatment": {"values": "string",
                                        "*": 0,
                                        "text": "Сведения об обработке от паразитов ('Дата Препарат Доза' по порядку)"},
                "vaccinations": {"values": "string",
                                 "*": 0,
                                 "text": "Сведения о вакцинации ('Дата Вид вакцины № серии' по порядку"},
                "medical_checkup_date": {"values": "string", "*": 0, "text": "Дата мед. осмотра"},
                "anamnesis": {"values": "string", "*": 0, "text": "Анамнез"},

            })
        else:
            return Response({"status": "Отказано в доступе"})

    def post(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        if worker.position not in ("a", "w"):
            return Response({"data": "Отказано в доступе"})
        shelter = worker.shelter
        data = request.data

        socialized = True if data["socialized"] == "true" else False

        sex = "m" if data["sex"] == "Мужской" else "f"

        if data["size"] == "Маленький":
            size = "s"
        elif data["size"] == "Средний":
            size = "m"
        else:
            size = "l"

        changed = "сохранено"

        try:
            animal = Animal.objects.get(animal_accounting_card=data["animal_accounting_card"])
            animal.delete()
            changed = "изменено"
        except Animal.DoesNotExist:
            pass

        try:
            new_animal = Animal(animal_accounting_card=data["animal_accounting_card"], kind=data["kind"],
                                birth_date=data["birth_date"], weight=float(data["weight"]), shelter=shelter,
                                name=data["name"], sex=sex, breed=data["breed"], cage_number=int(data["cage_number"]),
                                color=data["color"], hair=data["hair"], ears=data["ears"], tail=data["tail"],
                                size=size, identifying_marks=data["identifying_marks"],
                                animal_id=data["animal_id"], sterilization_date=data["sterilization_date"],
                                doctor_name=data["doctor_name"], socialized=socialized, region=data["region"],
                                catching_act_order=data["catching_act_order"], catching_act_date=data["catching_act_date"],
                                catching_act=data["catching_act"], catching_address=data["catching_address"],
                                legal_entity=data["legal_entity"], owner_name=data["owner_name"],
                                person_owner_name=data["person_owner_name"], entrance_act_date=data["entrance_act_date"],
                                entrance_act=data["entrance_act"], leaving_act_date=data["leaving_act_date"],
                                leaving_act_reason=data["leaving_act_reason"],
                                staff_name=data["staff_name"], parasites_treatment=data["parasites_treatment"],
                                vaccinations=data["vaccinations"], medical_checkup_date=data["medical_checkup_date"],
                                anamnesis=data["anamnesis"]
                                )
            new_animal.save()
            return Response({"data": f"Животное успешно {changed}"})
        except:
            return Response({"data": "Ошибка"})


class AdminReport(APIView):
    def get(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        animal_accounting_card = request.GET.get("animal_accounting_card", "---------")
        if worker.position == "d":
            shelters = ""
        elif worker.position == "w" or worker.position == "a":
            shelters = worker.shelter.name
        else:
            shelters = "---------"
        card = Animal.objects.get(animal_accounting_card=animal_accounting_card, shelter__name__contains=shelters)
        try:
            docx_export(card)
            return Response({"status": "ok"})
        except:
            return Response({"status": "не удалось((("})
