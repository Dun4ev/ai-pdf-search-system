# **AI-Powered PDF Search Engine**

This project enables semantic search and question-answering over the content of PDF documents using a Retrieval-Augmented Generation (RAG) architecture and large language models.

## **How It Works**

The process consists of two main stages:

1.  **Indexing:** Documents from the `test_doc/` folder are processed, split into logical chunks, converted into numerical vectors (embeddings), and stored in a local vector database (FAISS).
2.  **Search and Generation:** A user enters a query through the web interface. The system converts the query into a vector, finds the most relevant chunks in the database, and passes them along with the original query to a large language model (LLM) to generate a meaningful and contextual answer.

## **Installation**

1.  **Clone the repository** (if the project is in Git):
    ```bash
    git clone <REPOSITORY_URL>
    cd <project_folder>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # For Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Keys:**
    Create a `.env` file in the project's root directory and add your API key:
    ```
    OPENAI_API_KEY="sk-..."
    ```

## **Usage**

1.  **Add Documents:** Place your PDF files into the `test_doc/` folder.
2.  **Run Indexing:** Execute the scripts in strict order to create or update the search index.
    *This step must be repeated every time you add or modify documents.*
    ```bash
    python ingest1.py
    python chunk2.py
    python embed3.py
    python index4.py
    ...
    ```
3.  **Launch the Web Application:**
    ```bash
    streamlit run app7.py
    ```
4.  **Start Searching:** Open the address that appears in your terminal (usually `http://localhost:8501`) in your browser, enter your question, and get the answer.

## **Project Structure**

-   `ingest1.py`: Responsible for loading and reading PDF files from the `test_doc/` folder.
-   `chunk2.py`: Splits the extracted text into small, logically coherent chunks.
-   `embed3.py`: Converts text chunks into vector representations (embeddings) using a neural network model.
-   `index4.py`: Creates and saves a FAISS index from the generated vectors for fast searching.
-   `search5.py`: Implements the logic for searching relevant chunks in the index based on the query's vector representation.
-   `generate6.py`: Forms a prompt from the query and the found chunks and sends it to the LLM to generate the final answer.
-   `app7.py`: The main application file that integrates all components into a single web interface using Streamlit.
-   `requirements.txt`: A list of all libraries required for the project to run.
-   `.env`: A file for storing secret keys and environment variables.
-   `test_doc/`: The directory for storing the source PDF documents.
