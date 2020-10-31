from django.shortcuts import render
from django.views.decorators.http import require_GET
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django.contrib.auth import get_user_model
import os
from openpyxl import load_workbook
from datetime import datetime


class AdminView(APIView):
    def get(self, request):
        user = request.user
        worker = Worker.objects.get(user=user)
        shelter = worker.shelter
        if worker.position == "w":
            animals = Animal.objects.filter(shelter=shelter)
            serializer = AnimalSerializer(animals, many=True)
            return Response({"data": serializer.data})
        elif worker.position == "a":
            return Response({"data": "Это админ приюта"})
        return Response({"data": "ok"})


class ParseDataSet(APIView):
    def post(self, request):
        path = os.path.join("C:\\Users\Артур\Desktop", "Data set.xlsx")
        load_data_set(path)
        return Response({"ok": "ok"})




def load_data_set(path):
    wb = load_workbook(path)

    sheet = wb.get_sheet_by_name("Лист")

    array = []
    i = 1
    for cellObj in sheet['A3':'BC244']:  # диапазон для сведений о животных
        array.append(cellObj)

    if len(array) != 0:
        for line in array:
            birth_date = str(line[3].value).strip().replace("-", '.')
            obj = Animal(animal_accounting_card=line[1].value, kind=line[2].value, birth_date=get_birth_day(birth_date),
                         weight=float(line[4].value), name=line[5].value, sex=line[6].value, breed=line[7].value,
                         color=line[8].value, hair=line[9].value, ears=line[10].value, tail=line[11].value,
                         size=line[12].value, identifying_marks=get_bool(line[13].value),
                         cage_number=int(line[14].value),
                         animal_id=int(line[15].value),
                         sterilization_date=get_sterilization_date(str(line[16].value).strip("00:00:00")),
                         doctor_name=line[17].value, socialized=get_bool(line[18].value),
                         catching_act_order=line[19].value,
                         catching_act_date=get_act_date(str(line[20].value)), region=line[21].value,
                         catching_act=line[22].value,
                         catching_address=line[23].value, legal_entity=line[24].value, owner_name=line[27].value,
                         person_owner_name=line[30].value,
                         entrance_act_date=get_act_date(str(line[36].value)), entrance_act=line[37].value,
                         leaving_act_date=line[37].value,
                         leaving_act_reason=line[39].value, leaving_act=line[40].value, staff_name=line[44].value,
                         parasites_treatment=get_parasites_treatment(line[46].value, line[47].value, line[48].value),
                         )
            obj.save()


def get_birth_day(birth_date):
    dateFormatFrom = "%Y.%m.%d"
    dateFormatTo = "%d.%m.%Y"
    if len(birth_date.split(".")) == 1:
        birth_date = f"01.01.{birth_date}"
    else:
        birth_date = datetime.strptime(str(birth_date[:10]), dateFormatFrom)
        birth_date = birth_date.strftime(dateFormatTo)
    return birth_date


def get_bool(field):
    return True if field == "да" else False


def get_sterilization_date(sterilization_date):
    dateFormatFrom = "%Y-%m-%d"
    dateFormatTo = "%d.%m.%Y"
    if len(sterilization_date) > 11:
        return sterilization_date
    else:
        if "." in sterilization_date:
            dateFormatFrom = "%d.%m.%Y"
        else:
            dateFormatFrom = "%Y-%m-%d"
        sterilization_date = datetime.strptime(str(sterilization_date[:10]), dateFormatFrom)
        sterilization_date = sterilization_date.strftime(dateFormatTo)
        return str(sterilization_date)


def get_act_date(act_date):
    # dateFormatFrom = "%d.%m.%Y"
    dateFormatTo = "%d.%m.%Y"
    act_date.strip()
    if act_date == "None":
        return None
    else:
        act_date = str(act_date).strip("00:00:00")
        # if "." in act_date:
        #     dateFormatFrom = "%d.%m.%Y"
        # else:
        #     dateFormatFrom = "%Y-%m-%d"
        # act_date = datetime.strptime(act_date[:10], dateFormatFrom)
        # act_date = act_date.strftime(dateFormatTo)
    return act_date


def get_parasites_treatment(data, kind_med, dose):
    return f"{data} {kind_med}, {dose}"


