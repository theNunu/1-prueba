import fitz  # PyMuPDF #pip install PyMuPDF
import os

def read_pdf(file_path):
    """
    Lee un archivo PDF y muestra su contenido en la consola usando PyMuPDF.
    
    Args:
        file_path (str): Ruta al archivo PDF que se desea leer.
    """
    print(f"Intentando leer: {file_path}")
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe. Saltando este archivo.")
        return

    try:
        # Abrir el documento PDF
        doc = fitz.open(file_path)
        # Verificar el número total de páginas
        num_pages = doc.page_count
        print(f"Número total de páginas: {num_pages}")
        
        # Verificar si el PDF está encriptado
        if doc.is_encrypted:
            print(f"ADVERTENCIA: El archivo {os.path.basename(file_path)} está encriptado. Proporciona una contraseña si es necesario.")
            # Para desbloquear, usa doc.authenticate('contraseña') si la conoces
        
        # Leer y mostrar el texto de cada página
        for page_num in range(num_pages):
            page = doc.load_page(page_num)  # Carga la página por su índice (0-based)
            text = page.get_text()
            file_name = os.path.basename(file_path)
            print(f"\n--- Página {page_num + 1} de {file_name} ---")
            print(f"Texto extraído: {text}")
        
        # Cerrar el documento para liberar recursos
        doc.close()
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        return

if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio donde está el script
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(f"Directorio base del script: {base_path}")
    
    # Definir la carpeta dentro del proyecto donde están los PDFs
    pdf_folder = "download_folder"
    download_folder = os.path.join(pdf_folder)
    print(f"Ruta de la carpeta de PDFs: {download_folder}")
    
    # Verificar si la carpeta existe
    if not os.path.exists(download_folder):
        print(f"La carpeta {download_folder} no existe. Verifica el nombre o crea la carpeta.")
        print("Crea la carpeta 'download_folder' en el mismo directorio que este script.")
        exit()

    # Procesar todos los archivos PDF en la carpeta
    for filename in os.listdir(download_folder):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(download_folder, filename)
            print(f"\nProcesando archivo: {filename}")
            read_pdf(file_path)