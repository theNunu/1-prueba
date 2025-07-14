from pdf2image import convert_from_path #pdf2image convierte PDFs a imágenes
import pytesseract
import os
#python.exe -m pip install --upgrade pip
#pip install pdf2image pytesseract pillow
def read_pdf(file_path):
    """
    Lee un archivo PDF y muestra su contenido en la consola usando OCR con pdf2image y pytesseract.
    
    Args:
        file_path (str): Ruta al archivo PDF que se desea leer.
    """
    print(f"Intentando leer: {file_path}")
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe. Saltando este archivo.")
        return

    try:
        # Convertir el PDF a imágenes (una por página)
        images = convert_from_path(file_path)
        file_name = os.path.basename(file_path)
        print(f"Número total de páginas detectadas: {len(images)}")
        
        # Extraer texto de cada imagen usando OCR
        for page_num, image in enumerate(images, 1):
            text = pytesseract.image_to_string(image)
            print(f"\n--- Página {page_num} de {file_name} ---")
            print(f"Texto extraído: {text}")
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