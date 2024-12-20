import pandas as pd
import json
import os
from config import Config  # Importa a configuração

class PDFOutputHandler:
    def __init__(self):
        self.csv_path = os.path.join(Config.PROCESSED_DECRYPTED_FOLDER, "resultado_extracao.csv")
        self.json_folder = os.path.join(Config.PROCESSED_DECRYPTED_FOLDER, "json_outputs")
        os.makedirs(self.json_folder, exist_ok=True)

    def save_to_csv(self, dataframe):
        """Salva o DataFrame no CSV com modo append."""
        if not dataframe.empty:
            mode = 'a' if os.path.exists(self.csv_path) else 'w'
            header = not os.path.exists(self.csv_path)
            dataframe.to_csv(self.csv_path, mode=mode, header=header, index=False)
            print(f"Dados adicionados ao CSV: {self.csv_path}")
        else:
            print("Nenhum dado a salvar no CSV.")

    def save_to_json(self, dataframe):
        """Salva cada linha do DataFrame em um arquivo JSON separado."""
        for index, row in dataframe.iterrows():
            pdf_name = row.get("pdf_name", f"pdf_{index}")  # Garante um nome padrão se "pdf_name" estiver ausente
            json_path = os.path.join(self.json_folder, f"{pdf_name}.json")
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(row.to_dict(), json_file, ensure_ascii=False, indent=4)
            print(f"Dados salvos em JSON: {json_path}")