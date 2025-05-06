import os
import sys
from pdfminer.high_level import extract_text

def extract_and_save_text(pdf_path, output_dir=None):
    """
    Extrae el texto de un archivo PDF y lo guarda en un archivo TXT
    
    Args:
        pdf_path (str): Ruta al archivo PDF
        output_dir (str, opcional): Directorio donde guardar el archivo TXT.
                                  Si es None, se guarda en el mismo directorio del PDF.
    
    Returns:
        str: Ruta al archivo TXT generado
    """
    try:
        # Extraer el texto del PDF
        text = extract_text(pdf_path)
        
        # Determinar la ruta de salida
        base_name = os.path.basename(pdf_path)
        file_name_without_ext = os.path.splitext(base_name)[0]
        
        if output_dir is None:
            output_dir = os.path.dirname(pdf_path)
            if not output_dir:
                output_dir = '.'
        
        output_path = os.path.join(output_dir, f"{file_name_without_ext}.txt")
        
        # Guardar el texto en un archivo
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"Texto extraído y guardado en: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error al procesar {pdf_path}: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Función principal"""
    # Obtener los archivos PDF del directorio actual
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No se encontraron archivos PDF en el directorio actual.")
        return
    
    print(f"Se encontraron {len(pdf_files)} archivos PDF:")
    for i, pdf in enumerate(pdf_files, 1):
        print(f"  {i}. {pdf}")
    
    # Crear directorio para los archivos TXT si no existe
    output_dir = "pdf_extracted_text"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Procesar cada PDF
    for pdf in pdf_files:
        print(f"\nProcesando: {pdf}")
        pdf_path = os.path.join('.', pdf)
        extract_and_save_text(pdf_path, output_dir)
    
    print("\nProceso completado.")
    print(f"Los archivos de texto extraídos se encuentran en el directorio: {output_dir}")
    print("Puede revisar estos archivos para copiar y pegar los datos relevantes a la plantilla Excel.")

if __name__ == "__main__":
    main() 