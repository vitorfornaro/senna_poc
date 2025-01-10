import os
import shutil
import re
from PyPDF2 import PdfReader
from config import Config

class PDFTextExtractor:
    def __init__(self, input_folder=Config.DECRYPTED_FOLDER, processed_folder=Config.PROCESSED_DECRYPTED_FOLDER):
        self.input_folder = input_folder
        self.processed_folder = processed_folder

    def extract_text_from_pdfs(self):
        pdf_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith(".pdf")]
        if not pdf_files:
            print("Nenhum PDF encontrado na pasta de entrada.")
            return {}

        pdfs_text = {}  # Dicionário para armazenar textos de cada PDF

        for file_name in pdf_files:
            input_pdf_path = os.path.join(self.input_folder, file_name)
            processed_pdf_path = os.path.join(self.processed_folder, file_name)
            try:
                full_text = ""
                reader = PdfReader(input_pdf_path)
                for idx, page in enumerate(reader.pages):
                    full_text += f"------------------ PAGINA {idx} ----------------\n"
                    page_text = page.extract_text() or ""
                    full_text += page_text

                # Dividir o texto baseado no delimitador
                paginas = re.split(r"------------------ PAGINA \d+ ----------------", full_text)
                paginas = [pagina.strip() for pagina in paginas if pagina.strip()]

                print(f"\nTotal de páginas detectadas em '{file_name}': {len(paginas)}\n")

                # Armazena as páginas deste PDF no dicionário
                pdfs_text[file_name] = {f"texto_pagina{idx+1}": pag for idx, pag in enumerate(paginas)}

            except Exception as e:
                print(f"Ocorreu um erro ao processar '{file_name}': {e}")
            finally:
                # Mover o PDF processado para a pasta de processados
                shutil.move(input_pdf_path, processed_pdf_path)
                print(f"PDF '{file_name}' movido para a pasta de processados: {processed_pdf_path}")
        
        return pdfs_text