# search.py
# Импортируем pickle для загрузки сохранённых данных
import pickle
# Импортируем faiss для поиска по векторам
import faiss
# Импортируем SentenceTransformer для создания эмбеддингов запросов
from sentence_transformers import SentenceTransformer

# Загружаем модель для эмбеддинга запросов
model = SentenceTransformer('all-MiniLM-L6-v2')
# Загружаем индекс FAISS
index = faiss.read_index("docs.index")
# Загружаем чанки документов
chunks = pickle.load(open("chunks.pkl", "rb"))

# Функция для поиска по документам
# query: строка запроса
# top_k: количество лучших результатов
# Возвращает список найденных чанков
def search_docs(query, top_k=3):
    q_vector = model.encode([query])  # Получаем эмбеддинг запроса
    distances, indices = index.search(q_vector, top_k)  # Ищем ближайшие векторы
    return [chunks[i] for i in indices[0]]  # Возвращаем найденные чанки

# Точка входа при запуске скрипта напрямую
if __name__ == "__main__":
    results = search_docs("Explain transfer learning")  # Пример поиска
    for r in results:
        print(f"{r['filename']}:\n{r['text'][:300]}...\n")  # Выводим результаты