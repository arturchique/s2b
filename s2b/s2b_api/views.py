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
        """
        Возвращает данные о животном по animal_accounting_card -- уникальной карточке животного,
        если оно доступно для ролевой модели текущего пользователя

        формат запроса: s2b/api/v1/admin/?animal_accounting_card=<карточка>
        header: Authorization: Token <токен>
        """
        user = request.user
        animal_accounting_card = request.GET.get("animal_accounting_card", "---------")
        worker = Worker.objects.get(user=user)
        shelter = worker.shelter
        try:
            animal = Animal.objects.get(animal_accounting_card=animal_accounting_card, shelter=shelter)
            serializer = AdminAnimalSerializer(animal)
            return Response({"data": serializer.data})
        except:
            return Response({"data": "Такого животного не существует"})

    def post(self, request):
        """
        Возвращает список с данными обо всех животных, доступных для ролевой модели текущего пользователя,
        подходящих под фильтры (фильтры пока не реализованы, выдает только всех животных, если фильтры пусты)

        формат запроса: s2b/api/v1/admin/
        header: Authorization: Token <токен>
        body:
            filters: "" <-- должно быть пусто на текущий момент
            page: "страница"
            search: "номер карточки"  <-- вернет животного с заданным номером карточки, если не оставить поле пустым
        """
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
                serializer = AdminAnimalSerializer(paged_listings, many=True)
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
        """
        Возвращает список полей животных, нужных для заполнения пользователем (если он имеет доступ),
        чтобы добавить животного в базу

        формат запроса: s2b/api/v1/admin/add/
        header: Authorization: Token <токен>
        """
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
        """
        Создает животное в базе данных (если пользователь имеет доступ к созданию животного)

        формат запроса: s2b/api/v1/admin/add/
        header: Authorization: Token <токен>
        body: заполненные данными ключи из предыдущего запроса
        """
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
        """
        Создает отчетный документ по животному с заданным номером карточки, возвращает ссылку на него
        (Если пользователь имеет доступ по иерархии)

        формат запроса: s2b/api/v1/admin/report/
        header: Authorization: Token <токен>
        body: animal_accounting_card = номер карточки животного
        """
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
            path = docx_export(card)
            return Response({"path": path})
        except:
            return Response({"status": "не удалось((("})


class AdminDeleteView(APIView):
    def post(self, request):
        """
        Удаляет животное с заданным номером карточки, если пользователь имеет доступ

        формат запроса: s2b/api/v1/admin/delete/
        header: Authorization: Token <токен>
        body: animal_accounting_card = номер карточки животного
        """
        user = request.user
        worker = Worker.objects.get(user=user)
        if worker.position not in ("a", "w"):
            return Response({"data": "Отказано в доступе"})
        shelter = worker.shelter
        data = request.data
        deleted = "не удалено"
        try:
            animal = Animal.objects.get(animal_accounting_card=data["animal_accounting_card"], shelter=shelter)
            animal.delete()
            deleted = "удалено"
        except Animal.DoesNotExist:
            pass
        return Response({"data": f"Животное {deleted}"})


class HelloView(APIView):
    """
    Hello World!)))))
    """
    def get(self, request):
        return Response({"data": "Hello World"})


class TopSixAnimalsView(APIView):
    def get(self, request):
        """
        Возвращает список из шести животных готовых к социализации (Фронтенд-Пользовательский)
        """
        animals = Animal.objects.all()[:6]
        serializer = AnimalSerializer(animals, many=True)
        return Response({"Status": "Ok", "data": serializer.data})


class AnimalView(APIView):
    def get(self, request, animal_accounting_card):
        """
        Возвращает конкретное животное по номеру карточки (Фронтенж-Пользовательский)
        """
        animal = Animal.objects.get(animal_accounting_card=animal_accounting_card)
        serializer = AnimalSerializer(animal)
        return Response({"Status": "Ok", "data": serializer.data})


class AnimalFilterView(APIView):
    def post(self, request):
        """
        Возвращает отфильтрованный список животных. Если поле filter пустое, то возвращает всех зверей,
        готовых к социализации и списсок фильтров для отрисовки на странице

        формат:
        filters: либо пустое поле, либо объект полученный при передаче запроса с пустым полем
        search: поисковой запрос
        page: номер страницы (для пагинации)
        """
        if not request.data["filters"]:
            search_request = request.data["search"]
            animals = Animal.objects.filter(name__contains=search_request, socialized=True)
            paginator = Paginator(animals, 15)
            page = request.data["page"]
            paged_listings = paginator.get_page(page)
            serializer = AnimalSerializer(paged_listings, many=True)
            color_dict = dict()
            for color in ANIMAL_COLOR_CHOICES:
                color_dict[color[0]] = False
            return Response({
                "status": "ok",
                "filters": {
                    "kind": {"c": False, "d": False},
                    "sex": {"m": False, "f": False},
                    "size": {"s": False, "m": False, "l": False},
                    "color": color_dict
                },
                "animals": serializer.data,
                "total_page_count": paginator.num_pages,
            })
        else:
            data = request.data["filters"]
            search_request = request.data["search"]

            animal_kind = []
            if data["animal_kind"]["c"]:
                animal_kind.append("c")
            if data["animal_kind"]["d"]:
                animal_kind.append("d")
            if not animal_kind:
                animal_kind = ["c", "d"]

            animal_sex = []
            if data["animal_sex"]["m"]:
                animal_sex.append("m")
            if data["animal_sex"]["f"]:
                animal_sex.append("f")
            if not animal_sex:
                animal_sex = ["m", "f"]

            animal_size = []
            if data["animal_size"]["s"]:
                animal_size.append("s")
            if data["animal_size"]["m"]:
                animal_size.append("m")
            if data["animal_size"]["l"]:
                animal_size.append("l")
            if not animal_size:
                animal_size = ["s", "m", "l"]

            color_list = []
            for key, value in data["color"]:
                if value:
                    color_list.append(key)

            animals = Animal.objects.filter(name__contains=search_request,
                                            kind__in=animal_kind,
                                            sex__in=animal_sex,
                                            animal_size__in=animal_size,
                                            color__in=color_list,
                                            socialized=True)
            paginator = Paginator(animals, 15)
            page = request.data["page"]
            paged_listings = paginator.get_page(page)
            serializer = AnimalSerializer(paged_listings, many=True)
            return Response({
                "status": "ok",
                "filters": request.data["filters"],
                "animals": serializer.data,
                "total_page_count": paginator.num_pages
            })


class ClientsApplicationsView(APIView):
    def get(self, request, user_id):
        """

        Заявки клиента, не доделано
        """
        user = User.objects.get(id=user_id)
        client = Client.objects.get(user=user)
        applications = Application.objects.filter(client=client)

    def post(self, request):
        """
        Заявки клиента, не доделано
        """
        user = request.user
        client = Client.objects.get(user=user)
        animal = Animal.objects.get(animal_id=request.data["id"])
        application = Application(client=client, animal=animal,
                                  date=datetime.now(), quiz=request.data["answers"],
                                  status="r")
        application.save()
        return Response({"status": "ok"})
