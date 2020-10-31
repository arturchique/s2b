import os
from openpyxl import load_workbook
# from .models import *
from datetime import datetime


def load_data_set(path):
    wb = load_workbook(path)

    sheet = wb.get_sheet_by_name("Лист")

    array = []
    for cellObj in sheet['A3':'AT244']:  # диапазон для сведений о животных
        array.append(cellObj)

    if len(array) != 0:
        for line in array:
            birth_date = str(line[3].value).strip()
            if len(birth_date.split("/")) == 1:
                birth_date = f"01.01.{birth_date}"
            birth_date = datetime.strptime(birth_date, "%x")

        #     obj = Animal(animal_accounting_card=line[1].value, kind=line[2].value, birth_date=line[3].value,
        #                  weight=line[4].value, name=line[5].value, sex=line[6].value, breed=line[7].value,
        #                  color=line[8].value, hair=line[9].value, ears=line[10].value, tail=line[11].value,
        #                  size=line[12].value, identifying_marks=line[13].value, cage_number=line[14].value,
        #                  animal_id=line
        #                  )
        #     obj.save()
        # print(line[1].value, line[2].value, line[3].value, line[4].value, line[5].value, line[6].value,
        #       line[7].value, line[8].value, line[9].value, line[10].value, line[11].value, line[12].value,
        #       line[13].value, line[14].value, line[15].value, line[16].value, line[17].value, line[18].value,
        #       line[19].value, line[20].value, line[21].value, line[22].value, line[23].value, line[24].value,
        #       line[25].value, line[26].value, line[27].value, line[28].value, line[29].value, line[30].value,
        #       line[31].value, line[32].value, line[33].value, line[34].value, line[35].value, line[36].value,
        #       line[37].value, line[38].value, line[39].value, line[40].value, line[41].value, line[42].value,
        #       line[43].value, line[44].value, line[45].value)
            print(birth_date)


# load_data_set()
path = os.path.join("C:\\Users\Артур\Desktop", "Data set.xlsx")

load_data_set(path)
