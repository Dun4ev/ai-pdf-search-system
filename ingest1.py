# ingest.py
# Импортируем библиотеку для работы с PDF (PyMuPDF)
import fitz
# Импортируем модуль для работы с файловой системой
import os

# Функция для извлечения текста из всех PDF-файлов в указанной папке
# folder: путь к папке с PDF-файлами
# Возвращает список словарей с именем файла и текстом

def extract_text_from_pdfs(folder):
    documents = []  # Список для хранения результатов
    for file in os.listdir(folder):  # Перебираем все файлы в папке
        if file.endswith(".pdf"):  # Проверяем, что файл — PDF
            path = os.path.join(folder, file)  # Получаем полный путь к файлу
            text = ""  # Переменная для накопления текста
            pdf = fitz.open(path)  # Открываем PDF-файл
            for page in pdf:  # Перебираем все страницы PDF
                text += page.get_text()  # Извлекаем текст со страницы
            documents.append({"filename": file, "text": text})  # Добавляем результат в список
            print(f"✅ {file} - {len(text)} chars")  # Выводим информацию о файле
    return documents  # Возвращаем список документов

# Если скрипт запущен напрямую, а не импортирован как модуль
if __name__ == "__main__":
    # Извлекаем текст из всех PDF в папке ./test_doc
    docs = extract_text_from_pdfs("./test_doc")