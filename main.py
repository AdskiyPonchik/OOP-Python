import pandas as pd
import re
import os
data = {'Добродетели': ['Воздержание', 'Молчание', "Порядок", "Решительность", "Бережливость",
                        "Трудолюбие", "Искренность", 'Справедливость', "Умеренность", "Чистота",
                        "Спокойствие", "Целомудрие", "Скромность"],
        "MO": "",
        "TU": "",
        "WED": "",
        "THU": "",
        "FRI": "",
        "SAT": "",
        "SU": ""}
df = pd.DataFrame(data)
files_name = os.listdir('./')
xlsx_files = [file for file in files_name if file.endswith('.xlsx')]
numbers = list()
for i in xlsx_files:
    numbers = re.findall(r'\d+', i)
if len(numbers) == 0:
    number = 1
else:
    number = int(max(numbers)) + 1
df.to_excel(f'franklin_table_week_{number}.xlsx', index=False)