import streamlit as st
import os
import subprocess

def save_to_file(text, filename="user_input.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")

def commit_and_push():
    try:
        # Настраиваем имя пользователя и email для Git
        subprocess.run(["git", "config", "--global", "user.name", "aiken-kazin"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "aikenkazin@gmail.com"], check=True)
        
        # Обновляем локальный репозиторий перед коммитом
        subprocess.run(["git", "pull", "--rebase"], check=True)
        
        # Добавляем изменения и пушим
        subprocess.run(["git", "add", "user_input.txt"], check=True)
        subprocess.run(["git", "commit", "-m", "Update user input"], check=True)
        subprocess.run(["git", "push"], check=True)
        st.success("Файл успешно сохранен и отправлен в GitHub!")
    except subprocess.CalledProcessError as e:
        st.error(f"Ошибка при отправке в GitHub: {e}")

st.title("Сохранение текста в файл и GitHub")

user_input = st.text_area("Введите текст:")

if st.button("Отправить"):
    if user_input.strip():
        save_to_file(user_input)
        commit_and_push()
    else:
        st.warning("Введите текст перед отправкой!")

# if st.button("Показать сохраненный текст"):
#     try:
#         with open("user_input.txt", "r", encoding="utf-8") as file:
#             content = file.read()
#         st.text_area("Содержимое файла:", content, height=300)
#     except FileNotFoundError:
#         st.warning("Файл пока пуст или не найден.")