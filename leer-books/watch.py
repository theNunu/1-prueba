from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Ruta a la base de datos vectorial
CHROMA_DIR = "vector_store"

# Cargar embeddings (debe ser el mismo modelo que usaste al guardar)
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Cargar el vector store ya existente
vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

# Función para mostrar documentos y vectores
def ver_contenido_vector_store(n=5):
    # Consulta n documentos similares a una palabra cualquiera (para probar)
    resultados = vectorstore.similarity_search("libro", k=n)
    for i, doc in enumerate(resultados, 1):
        print(f"\n📄 Documento {i}:")
        print(doc.page_content[:300])  # Muestra los primeros 300 caracteres del fragmento
        print(f"🧾 Metadata: {doc.metadata}")
    
    # Mostrar los vectores numéricos (reales) del primer documento
    print("\n🔢 Mostrando algunos vectores numéricos:")
    vector = embedding.embed_query(resultados[0].page_content)
    print(vector[:10], "...")  # Muestra los primeros 10 valores del vector

# Llamamos la función
ver_contenido_vector_store()
