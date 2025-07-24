# app.py
# Импортируем streamlit для создания веб-интерфейса
import streamlit as st
# Импортируем функцию поиска по документам
from search5 import search_docs
# Импортируем функцию генерации ответа
from generate6 import ask

# Заголовок приложения
st.title(" 4da AI Document Search")
# Поле для ввода вопроса пользователя
query = st.text_input("Ask a question:")
if query:
    with st.spinner("Searching..."):
        top_chunks = search_docs(query)  # Ищем релевантные чанки
        context = "\n\n".join([c["text"] for c in top_chunks])  # Формируем контекст
        answer = ask(query, context)  # Получаем ответ
        st.write("**Answer:**")  # Заголовок для ответа
        st.write(answer)  # Выводим ответ