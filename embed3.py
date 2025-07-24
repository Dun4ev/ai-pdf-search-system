# embed.py
# Импортируем SentenceTransformer для создания эмбеддингов
from sentence_transformers import SentenceTransformer
# Импортируем numpy для работы с массивами
import numpy as np

# Загружаем предобученную модель для эмбеддинга текстов
model = SentenceTransformer('all-MiniLM-L6-v2')

# Функция для преобразования чанков в векторные представления (эмбеддинги)
def embed_chunks(chunks):
    texts = [c["text"] for c in chunks]  # Извлекаем тексты из чанков
    vectors = model.encode(texts)  # Получаем эмбеддинги для всех текстов
    return np.array(vectors)  # Возвращаем как numpy-массив

# Точка входа при запуске скрипта напрямую
if __name__ == "__main__":
    from chunk2 import chunk_document
    from ingest1 import extract_text_from_pdfs
    docs = extract_text_from_pdfs("./test_doc")
    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_document(doc))
    vectors = embed_chunks(all_chunks)
    print(f" 705 Embedded shape: {vectors.shape}")  # Выводим форму массива эмбеддингов