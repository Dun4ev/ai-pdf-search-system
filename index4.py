# index.py
# Импортируем faiss для создания индекса поиска по векторам
import faiss
# Импортируем pickle для сохранения данных
import pickle

# Функция для построения FAISS-индекса по векторам
# vectors: numpy-массив эмбеддингов
# Возвращает индекс FAISS
def build_faiss_index(vectors):
    dim = vectors.shape[1]  # Определяем размерность векторов
    index = faiss.IndexFlatL2(dim)  # Создаём индекс с L2-метрикой
    index.add(vectors)  # Добавляем векторы в индекс
    return index

# Точка входа при запуске скрипта напрямую
if __name__ == "__main__":
    from embed3 import embed_chunks
    from chunk2 import chunk_document
    from ingest1 import extract_text_from_pdfs
    docs = extract_text_from_pdfs("./test_doc")
    all_chunks = []
    for doc in docs:
        all_chunks.extend(chunk_document(doc))
    vectors = embed_chunks(all_chunks)
    index = build_faiss_index(vectors)
    faiss.write_index(index, "docs.index")
    with open("chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)
    print(" 4e6 Index and metadata saved")