from PyPDF2 import PdfReader
import os #Importa el módulo os para verificar la existencia del archivo.



def read_pdf(file_path):
    """
    Lee un archivo PDF y muestra su contenido en la consola.
    
    Args:
        file_path (str): Ruta al archivo PDF que se desea leer.
    """
    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe. Verifica la ruta.")
        return

    # Crear un objeto PdfReader para leer el PDF
    reader = PdfReader(file_path)
    
    # Obtener el número total de páginas
    num_pages = len(reader.pages)
    print(f"El archivo contiene {num_pages} página(s).") #calcula cuántas páginas tiene el PDF y almacena ese número
    # len()  devuelve la longitud (número de elementos) de un objeto iterable, como una lista,
    #  tupla, diccionario, o en este caso, la colección de páginas de un PDF


    # Leer y mostrar el texto de cada página
    for page_num in range(num_pages): #Si num_pages es 3, range(3) genera [0, 1, 2]
        page = reader.pages[page_num]
        text = page.extract_text()
        print(f"\n--- Página {page_num + 1} ---")
        print(text)

if __name__ == "__main__":
    # Especifica la ruta al archivo PDF (ajústala según tu sistema)
    pdf_path  = r"C:\Users\USUARIO\Downloads\SNE_SOLICITUD_DE_EMPLEO_PLANTILLA_PDF.pdf" # Cambia esto por la ruta real de tu PDF
    read_pdf(pdf_path)


