import streamlit as st

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd



# Specify path to your file with credentials
path_to_credential = 'project2-453818-894de48f5133.json' 

# Specify name of table in google sheets
table_name = 'table'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(path_to_credential, scope)
gs = gspread.authorize(credentials)

work_sheet = gs.open(table_name)
sheet1 = work_sheet.sheet1

# data = sheet1.get_all_values()
# headers = data.pop(0)

# df = pd.DataFrame(data, columns=headers)
# print(df.head())





def save_text(text):
    """Сохраняет введенный текст в файл."""
    new_row = [text]
    sheet1.append_row(new_row)

# Заголовок приложения
st.title("Напишите анонимное сообщение")

# Поле для ввода текста
user_input = st.text_area("Введите текст:")

# Кнопка для отправки
if st.button("Отправит анонимное сообщение"):
    if user_input.strip():  # Проверяем, что текст не пустой
        save_text(user_input)
        st.success("Текст успешно отправлен!")
    else:
        st.warning("Введите текст перед отправлением.")