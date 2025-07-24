# chunk.py

# Функция для разбиения документа на части (чанки)
# doc: словарь с текстом и именем файла
# size: размер одного чанка (по умолчанию 1000 символов)
# overlap: перекрытие между чанками (по умолчанию 200 символов)
def chunk_document(doc, size=1000, overlap=200):
    text = doc["text"]
    chunks = []  # Список для хранения чанков
    start = 0
    while start < len(text):  # Пока не обработан весь текст
        end = start + size
        chunk = text[start:end]  # Вырезаем кусок текста
        chunks.append({
            "filename": doc["filename"],
            "text": chunk
        })  # Добавляем чанк в список
        start += size - overlap  # Сдвигаем окно с учетом перекрытия
    return chunks  # Возвращаем список чанков

# Точка входа при запуске скрипта напрямую
if __name__ == "__main__":
    from ingest1 import extract_text_from_pdfs  # Импорт функции для извлечения текста из PDF
    docs = extract_text_from_pdfs("./test_doc")  # Извлекаем документы из папки
    all_chunks = []  # Список для всех чанков
    for doc in docs:
        all_chunks.extend(chunk_document(doc))  # Разбиваем каждый документ на чанки
    print(f" 539 Created {len(all_chunks)} chunks")  # Выводим количество чанков