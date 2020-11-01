from docxtpl import DocxTemplate  # pip install docxtpl
from datetime import datetime


def docx_export(card):
    infile_path = "media/reports/animal_registration_card.docx"
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    context = {
        'animal_accounting_card': card.animal_accounting_card,
        'data_report': datetime.now,
        # 'shelter_address' : card.shelter_address, - нужно добавить к объекту
        # 'operating_organization' : card.operating_organization, - нужно добавить к объекту
        'cage_namber': card.cage_number,
        'kind': card.kind,
        'birth_date': card.birth_date,
        'weight': card.weight,
        'name': card.name,
        'sex': card.sex,
        'breed': card.breed,
        'color': card.color,
        'hair': card.hair,
        'ears': card.ears,
        'tail': card.tail,
        'size': card.size,
        'identifying_marks': card.identifying_marks,
        'animal_id': card.animal_id,
        'sterilization_date': str(card.sterilization_date.strftime("«%d»")) +
                              str(month_list[card.sterilization_date.month - 1].capitalize()) +
                              str(card.sterilization_date.strftime("%Y года")),
        'doctor_name': card.doctor_name,
        'socialized': card.socialized,
        'catching_act': card.catching_act,
        'catching_address': card.catching_address,
        'legal_entity': card.legal_entity,
        'owner_name': card.owner_name,
        'person_owner_name': card.person_owner_name,
        'entrance_act_date': str(card.entrance_act_date.strftime("«%d»")) +
                             str(month_list[card.entrance_act_date.month - 1].capitalize()) +
                             str(card.entrance_act_date.strftime("%Y года")),
        'entrance_act': card.entrance_act,
        'leaving_act_date': str(card.leaving_act_date.strftime("«%d»")) +
                            str(month_list[card.leaving_act_date.month - 1].capitalize()) +
                            str(card.leaving_act_date.strftime("%Y года")),
        'leaving_act': card.leaving_act,
        'leaving_act_reason': card.leaving_act_reason,
        'tbl_parasites': [
            {'num': '1', 'parasites': card.parasites_treatment}  # должно быть одной строкой
        ],
        'tbl_vaccinations': [
            {'num': '1', 'vaccinations': card.vaccinations}  # должно быть одной строкой
        ],
        'tbl_med_status': [
            {'num': '1', 'medical_checkup_date': card.medical_checkup_date,
             #    'weight' : card.medical_checkup.weight,  - нужно добавить к объекту
             'anamnesis': card.anamnesis
             }
        ],
        'staff_name': card.staff_name,
    }

    # ТЕСТОВЫЕ ДАННЫЕ ДЛЯ ВЫГРУЗКИ - такого формата должны быть данные

    # context = {
    #         'animal_accounting_card' : "1665з-20",
    #         'data_report' : str(now.strftime("«%d» ")) +
    #                         str(month_list[now.month - 1].capitalize()) +
    #                         str(now.strftime(" %Y года")),
    #         'shelter_address' : "Москва, ул. Строителей, д.12",
    #         'operating_organization' : "Название организации",
    #         'cage_namber' : "12345",
    #         'kind' : "Собака",
    #         'birth_date' : "5",
    #         'weight' : "3",
    #         'name'   : "Барсик",
    #         'sex' : "мужской",
    #         'breed' : "порода",
    #         'color' : "окрас",
    #         'hair' : "шерсть",
    #         'ears' : "полустоячии",
    #         'tail' : "обычный",
    #         'size' :  "крупный",
    #         'identifying_marks' : "нет",
    #         'animal_id' : "643094100661471",
    #         'sterilization_date' : "23.09.2020",
    #         'doctor_name' : "Ф.И.О. ветеринарного врача",
    #         'socialized' :  "да",
    #         'catching_act' : "12",
    #         'catching_address' : "Адрес места отлова",
    #         'legal_entity' : "Юридическое лицо",
    #         'owner_name' :  "Ф.И.О. опекунов",
    #         'person_owner_name' : "Физическое лицо (Ф.И.О.)",
    #         'entrance_act_date' : "27.09.2020",
    #         'entrance_act' : "123",
    #         'leaving_act_date' : "15.10.2020",
    #         'leaving_act' :  "45/1",
    #         'leaving_act_reason' : "Смерть",
    #         'tbl_parasites': [
    #                     {'num': '1', 'parasites' : '27.09.2020 Препарат Доза' },
    #                     {'num': '2', 'parasites' : "27.09.2020 Препарат Доза" },
    #                     {'num': '3', 'parasites' : "27.09.2020 Препарат Доза" },
    #                          ],
    #         'tbl_vaccinations': [
    #                     {'num': '1', 'vaccinations': "23.09.2020 Вакцина 0203"},
    #                     {'num': '2', 'vaccinations': "23.09.2020 Вакцина 0203"},
    #                     {'num': '3', 'vaccinations': "23.09.2020 Вакцина 0203"},
    #                          ],
    #         'tbl_med_status': [
    #                     {'num': '1', 'medical_checkup_date' : "11.10.2020", 'weight' : "5,5", 'anamnesis' :  "Анамез"},
    #                     {'num': '2', 'medical_checkup_date' : "11.10.2020", 'weight' : "5,5", 'anamnesis' :  "Анамез"},
    #                     {'num': '3', 'medical_checkup_date' : "11.10.2020", 'weight' : "5,5", 'anamnesis' :  "Анамез"},
    #                          ],
    #                  ]
    #         'staff_name' :  "Иванов Иван Иванович",
    #         }

    # animal_registration_card.docx
    doc = DocxTemplate(infile_path)
    doc.render(context)
    # нужно добавить адрес к директории где лежат фотки во 2 аргумент
    doc.replace_pic("media/photos/example.jpg", f"media/photos/{card.animal_accounting_car}.jpg")
    doc.save(f"media/reports/{card.animal_accounting_card}_{datetime.now().strftime('%d_%m_%Y_%H%M')}.docx")

