import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Читаем учетные данные из Streamlit Secrets
import json
credentials_info = json.loads(st.secrets["GOOGLE_CREDENTIALS"])

# Авторизация с Google Sheets API
credentials = Credentials.from_service_account_info(credentials_info, scopes=[
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
])

gs = gspread.authorize(credentials)

# Открываем Google Sheet
table_name = "table"
work_sheet = gs.open(table_name)
sheet1 = work_sheet.sheet1

def save_text(text):
    """Сохраняет введенный текст в Google Sheets."""
    sheet1.append_row([text])

# UI Streamlit
st.title("Напишите анонимное сообщение")
user_input = st.text_area("Введите текст:")

if st.button("Отправить анонимное сообщение"):
    if user_input.strip():
        save_text(user_input)
        st.success("Текст успешно отправлен!")
    else:
        st.warning("Введите текст перед отправкой.")
