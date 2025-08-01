import os
import time
import requests
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from pathlib import Path

# Configuración general
CHROMA_DIR = "vector_store"
os.makedirs(CHROMA_DIR, exist_ok=True)
MAX_LIBROS = 50  # Máximo de libros a subir
START_ID = 1     # ID inicial
END_ID = 10000   # ID final para recorrer
PAUSA_SEGUNDOS = 2  # Pausa entre cada descarga

# Embeddings (modelo local, no requiere API)
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Verifica si el texto está en español (técnica simple)
def es_espanol(texto):
    palabras_clave = ["el ", "la ", "de ", "que ", "y ", "en ", "los "]
    coincidencias = sum(1 for palabra in palabras_clave if palabra in texto.lower())
    return coincidencias >= 3  # Umbral ajustable

# Construye la URL del texto en Project Gutenberg
def construir_url(book_id):
    return f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"

# Descarga y valida si el libro está en español
def obtener_libro_espanol(book_id):
    url = construir_url(book_id)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        contenido = response.text
        # Verifica idioma en encabezado o contenido
        if 'Language: Spanish' in contenido or es_espanol(contenido[:1000]):
            print(f"✅ Libro {book_id} es en español.")
            return contenido
        else:
            print(f"⛔ Libro {book_id} no es en español.")
            return None
    except:
        print(f"⚠️ Error al intentar descargar libro {book_id}")
        return None

# División de texto
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documentos = []

# Recorremos IDs con pausa
contador = 0
for book_id in range(START_ID, END_ID):
    if contador >= MAX_LIBROS:
        break
    contenido = obtener_libro_espanol(book_id)
    if contenido:
        doc = Document(page_content=contenido, metadata={"book_id": book_id})
        partes = text_splitter.split_documents([doc])
        documentos.extend(partes)
        contador += 1
        print(f"📚 Libro {book_id} agregado. Total: {contador}")
        time.sleep(PAUSA_SEGUNDOS)

# Guardamos en ChromaDB
if documentos:
    vectorstore = Chroma.from_documents(documentos, embedding, persist_directory=CHROMA_DIR)
    vectorstore.persist()
    print(f"\n🎉 Se almacenaron {contador} libros en ChromaDB.")
else:
    print("\n❌ No se encontró ningún libro en español.")
