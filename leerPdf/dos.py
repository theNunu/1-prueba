from PyPDF2 import PdfReader
import os
import pdfplumber

def read_pdf(file_path):
    """
    Lee un archivo PDF y muestra su contenido en la consola.
    
    Args:
        file_path (str): Ruta al archivo PDF que se desea leer.
    """
    # Imprimir la ruta para depuración
    print(f"Intentando leer: {file_path}")
    
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe. Saltando este archivo.")
        return

    try:
        reader = PdfReader(file_path)
        num_pages = len(reader.pages) # Obtener el número total de páginas
        print(f"El archivo contiene {num_pages} página(s).")
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            print(f"\n--- Página {page_num + 1} de {os.path.basename(file_path)} ---")
            print(text)
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        print("Tipo de error: ", type(e).__name__)
        return  # Continúa con el siguiente archivo

if __name__ == "__main__":
    # Definir la carpeta dentro del proyecto donde están los PDFs
    pdf_folder = "download_folder"  # Ajusta este nombre si tu carpeta se llama diferente (ej. "documents")
    
    # Construir la ruta absoluta basada en el directorio actual del script
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    download_folder = os.path.join(pdf_folder)
    
    # Verificar si la carpeta existe
    if not os.path.exists(download_folder):
        print(f"La carpeta {download_folder} no existe. Verifica el nombre o crea la carpeta.")
        exit()

    # Listar todos los archivos en la carpeta
    for filename in os.listdir(download_folder):
        #os.listdir(download_folder) para obtener una lista de todos los archivos y carpetas dentro de download_folder.
        # Filtrar solo archivos PDF
        if filename.lower().endswith('.pdf'): #los archivos que terminan en .pdf
            # Construir la ruta completa del archivo
            file_path = os.path.join(download_folder, filename)
            """
            Cada llamada a os.path.join() genera una ruta única basada en el filename específico, 
            permitiendo que el script acceda a un archivo a la vez.
            """
            print(f"\nProcesando archivo: {filename}")
            read_pdf(file_path)

            """  Si download_folder contiene finalizado.pdf, documento.pdf, y nota.txt, os.listdir(download_folder)
            devuelve ['finalizado.pdf', 'documento.pdf', 'nota.txt'], y el filtro deja solo ['finalizado.pdf', 
            'documento.pdf']."""