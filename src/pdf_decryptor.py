import os
import shutil
import pikepdf
from config import Config

class PDFDecryptor:
    def __init__(self, source_folder=Config.ENCRYPTED_FOLDER, 
                 processed_folder=Config.PROCESSED_ENCRYPTED_FOLDER, 
                 target_folder=Config.DECRYPTED_FOLDER):
        self.source_folder = source_folder
        self.processed_folder = processed_folder
        self.target_folder = target_folder

    def decrypt_first_pdf(self):
        pdf_files = [f for f in os.listdir(self.source_folder) if f.lower().endswith('.pdf')]
        if not pdf_files:
            print("Nenhum arquivo PDF encontrado na pasta maps.")
            return None

        encrypted_pdf_path = os.path.join(self.source_folder, pdf_files[0])
        decrypted_pdf_path = os.path.join(self.target_folder, f"decrypted_{pdf_files[0]}")

        try:
            with pikepdf.open(encrypted_pdf_path) as pdf:
                pdf.save(decrypted_pdf_path)
            print(f"PDF desbloqueado com sucesso! Salvo em: {decrypted_pdf_path}")

            # Move o PDF original para a pasta processed
            shutil.move(encrypted_pdf_path, os.path.join(self.processed_folder, pdf_files[0]))
            print(f"PDF original criptografado movido para: {self.processed_folder}")

            return decrypted_pdf_path
        except pikepdf.PasswordError:
            print(f"O PDF '{pdf_files[0]}' está protegido por senha e não pode ser desbloqueado.")
        except FileNotFoundError as e:
            print(f"Erro: Arquivo não encontrado. {e}")
        except Exception as e:
            print(f"Ocorreu um erro ao descriptografar: {e}")
        
        return None