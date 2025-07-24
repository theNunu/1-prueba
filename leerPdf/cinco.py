<<<<<<< HEAD
=======

>>>>>>> 4d5b78d7d2129ce79b2d404337bf67c2079b4ad9
from pdf2image import convert_from_path
import pytesseract
import os
from tqdm import tqdm

<<<<<<< HEAD
=======

os.environ["PATH"] += os.pathsep + r'C:\poppler\Library\bin'

>>>>>>> 4d5b78d7d2129ce79b2d404337bf67c2079b4ad9
# Configuración de Tesseract y Poppler (ajusta según tu sistema)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
# os.environ["PATH"] += os.pathsep + r'C:\poppler-XX.XX.X\bin'  # Windows

def read_pdf(file_path, output_folder="output_texts"):
<<<<<<< HEAD
=======
    
>>>>>>> 4d5b78d7d2129ce79b2d404337bf67c2079b4ad9
    """
    Lee un archivo PDF y extrae su contenido usando OCR con pdf2image y pytesseract.
    Guarda el texto extraído en un archivo.

    Args:
        file_path (str): Ruta al archivo PDF que se desea leer.
        output_folder (str): Carpeta donde se guardarán los textos extraídos.
    """
    print(f"Intentando leer: {file_path}")
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe. Saltando este archivo.")
        return

    # Crear carpeta para los textos extraídos
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Convertir el PDF a imágenes (una por página)
        images = convert_from_path(file_path, dpi=300)
        file_name = os.path.basename(file_path)
        print(f"Número total de páginas detectadas: {len(images)}")

        # Preparar archivo de salida
        output_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}_output.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            # Extraer texto de cada imagen usando OCR
            for page_num, image in enumerate(tqdm(images, desc=f"Procesando {file_name}"), 1):
                text = pytesseract.image_to_string(image, lang='spa')  # Especificar idioma
                f.write(f"--- Página {page_num} de {file_name} ---\n")
                f.write(text + "\n\n")
                print(f"\n--- Página {page_num} de {file_name} ---")
                print(f"Texto extraído: {text}")
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        return

if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio donde está el script
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(f"Directorio base del script: {base_path}")

    # Definir la carpeta donde están los PDFs
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
            read_pdf(file_path, output_folder=os.path.join(base_path, "output_texts"))