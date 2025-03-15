import streamlit as st

def save_to_file(text, filename="user_input.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n\n")

st.title("Поделитесь своим мнением!! все анонимно")

user_input = st.text_area("Введите текст:")

if st.button("Отправить"):
    if user_input.strip():
        save_to_file(user_input)
        st.success("Ответ записан, спасибо что поделились мнением!!!")
    else:
        st.warning("Введите текст перед отправкой!")
