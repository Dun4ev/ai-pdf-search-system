#6 generate.py
import os
# Импортируем OpenAI для генерации ответов
from openai import OpenAI
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
import logging
logging.basicConfig(level=logging.INFO)
logging.info(f"Текущая директория: {os.getcwd()}")
logging.info(f"Файлы: {os.listdir()}")
logging.info(f"Значение ключа: {os.getenv('OPENAI_API_KEY')!r}")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Не задана переменная окружения OPENAI_API_KEY")
# Создаём клиента OpenAI
try:
    client = OpenAI(api_key=api_key)
except Exception as e:
    raise RuntimeError("Ошибка инициализации OpenAI: проверьте переменную окружения OPENAI_API_KEY") from e


# Функция для генерации ответа на вопрос с учётом контекста
# question: строка вопроса
# context: строка с контекстом (текст из документов)
def ask(question, context):
    prompt = f"""
Context:
{context}

Question: {question}

Ответ в коротком абзаце на русском языке.
"""  # Формируем промпт для модели
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )  # Отправляем запрос к модели
    return response.choices[0].message.content  # Возвращаем ответ

# Точка входа при запуске скрипта напрямую
if __name__ == "__main__":
    from search5 import search_docs  # Импортируем функцию поиска
    question = "Explain transfer learning"  # Пример вопроса
    top_chunks = search_docs(question)  # Ищем релевантные чанки
    context = "\n\n".join([c["text"] for c in top_chunks])  # Формируем контекст
    answer = ask(question, context)  # Получаем ответ
    print(" 4a1 Answer:", answer)  # Выводим ответ