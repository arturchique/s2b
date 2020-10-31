from django.db import models
import uuid
from django.contrib.auth import get_user_model
from datetime import datetime
from .glossary import *

User = get_user_model()


class Animal(models.Model):
    animal_accounting_card = models.CharField(
        primary_key=True, max_length=20, blank=False, help_text="Номер карточки учета животного",
        unique=True, verbose_name="Карточка учета животного"
    )
    kind = models.CharField(
        max_length=1, choices=ANIMAL_KIND_CHOICES, verbose_name="Вид животного",
        help_text="Вид животного", blank=False
    )
    birth_date = models.DateTimeField(
        verbose_name="Возраст, дата рождения", help_text="Возраст, дата рождения",
        auto_now=False, blank=False
    )
    weight = models.FloatField(max_length=5, verbose_name="Вес", help_text="Вес", blank=False)
    name = models.CharField(
        max_length=20, verbose_name="Кличка", help_text="Кличка", default="без клички",
        blank=False
    )
    sex = models.CharField(
        max_length=1, choices=ANIMAL_SEX_CHOICES, verbose_name="Пол", help_text="Пол",
        blank=True, null=True
    )
    breed = models.CharField(
        max_length=25, choices=ANIMAL_BREED_CHOICES, verbose_name="Порода",
        blank=False, null=False, default="метис", help_text="Порода"
    )
    color = models.CharField(
        max_length=25, choices=ANIMAL_COLOR_CHOICES, verbose_name="Цвет",
        blank=False, null=False, default="черный", help_text="Цвет"
    )
    hair = models.CharField(
        max_length=25, choices=ANIMAL_HAIR_CHOICES, verbose_name="Шерсть",
        blank=False, null=False, default="обычная", help_text="Шерсть"
    )
    ears = models.CharField(
        max_length=25, choices=ANIMAL_EAR_CHOICES, verbose_name="Уши",
        blank=False, null=False, default="стоячие", help_text="Уши"
    )
    tail = models.CharField(
        max_length=25, choices=ANIMAL_TAIL_CHOICES, verbose_name="Хвост",
        blank=False, null=False, default="обычный", help_text="Хвост"
    )
    size = models.CharField(
        max_length=1, choices=ANIMAL_SIZE_CHOICES, verbose_name="Размер",
        blank=False, null=False, default="средний", help_text="Размер"
    )
    identifying_marks = models.CharField(
        max_length=50, default="нет", help_text="Особые приметы",
        verbose_name="Особые приметы", blank=False
    )
    cage_number = models.IntegerField(verbose_name="Вольер N", help_text="Номер вольера", blank=True, null=True, )
    animal_id = models.BigIntegerField(
        verbose_name="Идентификационная метка", help_text="Идентификационная метка",
        unique=True, blank=False, null=True
    )
    sterilization_date = models.CharField(
        verbose_name="Дата стериллизации", null=True, max_length=40,
        help_text="Дата стериллизации", blank=False
    )
    doctor_name = models.CharField(
        max_length=50, help_text="ФИО вет. врача", verbose_name="ФИО врача",
        blank=True, null=True
    )
    socialized = models.BooleanField(
        default=False, verbose_name="Социализировано", help_text="Социализировано (да/нет)",
        blank=False, null=True
    )
    entrance_act = models.CharField(
        max_length=15, verbose_name="Акт о поступлении", help_text="Акт о поступлении",
        blank=False, null=True
    )
    leaving_act = models.CharField(
        max_length=15, verbose_name="Акт о выбытии", help_text="Акт о выбытии",
        blank=True, null=True
    )
    entrance_act_date = models.DateTimeField(
        auto_now=False, verbose_name="Акт о поступлении. Дата", null=True,
        help_text="Акт о поступлении. Дата", blank=False
    )
    leaving_act_date = models.DateTimeField(
        auto_now=False, verbose_name="Дата выбытия", null=True,
        help_text="Дата выбытия", blank=True
    )
    leaving_act_reason = models.CharField(
        max_length=1, choices=LEAVING_REASON_CHOICES, verbose_name="Причина выбытия",
        blank=True, null=True, help_text="Причина выбытия"
    )
    region = models.CharField(
        max_length=10, verbose_name="Административный округ", help_text="Административный округ",
        blank=False, null=True
    )
    catching_act = models.CharField(
        max_length=15, verbose_name="Акт отлова", help_text="Акт отлова",
        blank=True, null=True,
    )
    catching_address = models.CharField(
        max_length=15, verbose_name="Адрес места отлова", help_text="Адрес места отлова",
        blank=True, null=True,
    )
    legal_entity = models.CharField(
        max_length=15, verbose_name="Юридическое лицо", help_text="Юридическое лицо",
        blank=True, null=True
    )
    owner_name = models.CharField(
        max_length=15, verbose_name="ФИО опекунов", help_text="ФИО опекунов",
        blank=True, null=True
    )
    person_owner_name = models.CharField(
        max_length=15, verbose_name="ФИО физического лица", help_text="ФИО физического лица",
        blank=True, null=True
    )
    staff_name = models.CharField(
        max_length=15, verbose_name="ФИО сотрудника по уходу", help_text="ФИО сотрудника по уходу",
        blank=True, null=True
    )
    parasites_treatment = models.TextField(
        verbose_name="Обработка от эндо- и эктопаразитов", blank=True, max_length=500, null=True,
        help_text="Введите данные об обработке от паразитов в формате: дата, название препарата, доза"
    )
    vaccinations = models.TextField(
        verbose_name="Вакцины", blank=True, max_length=500, null=True,
        help_text="Введите данные о вакцинации в формате: дата, вид вакцины, номер серии"
    )
    medical_checkup_date = models.DateTimeField(
        verbose_name="Дата медосмотра", blank=True, auto_now=False,
        help_text="Дата медосмотра", null=True
    )
    anamnesis = models.CharField(verbose_name="Анамнез", blank=True, help_text="Анамнез", max_length=20, null=True)


class Shelter(models.Model):
    name = models.CharField(
        max_length=40, blank=False, verbose_name="Название приюта",
        help_text="Название приюта"
    )
    address = models.CharField(
        max_length=100, blank=False, verbose_name="Адресс приюта",
        help_text="Адресс приюта"
    )
    prefecture = models.CharField(
        max_length=80, blank=False, verbose_name="Подчинение",
        help_text="Подчинение (например: Префектура ЮВАО)"
    )
    phone_number = models.CharField(
        max_length=20, blank=True, verbose_name="Номер телефона",
        help_text="Номер телефона", null=True
    )
    animals = models.ManyToManyField(
        Animal, help_text="Животные", verbose_name="Животные",
        blank=False, null=True
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(
        verbose_name="Имя работника", help_text="Имя работника",
        max_length=30, blank=True, null=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Пользователь", null=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, help_text="Приют", verbose_name="Приют", blank=True)
    position = models.CharField(
        verbose_name="Должность", help_text="Должность", null=True,
        max_length=1, choices=WORKER_POSITIONS_CHOICES, blank=True
    )

