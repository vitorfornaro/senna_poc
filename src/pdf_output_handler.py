import pandas as pd
import json
import os
from config import Config  # Importa a configuração


class PDFOutputHandler:
    def __init__(self):
        # Define os caminhos das pastas de saída
        self.csv_folder = os.path.join(Config.MAPS_DIR, "outputs", "csv")
        self.json_folder = os.path.join(Config.MAPS_DIR, "outputs", "json")
        self.csv_path = os.path.join(self.csv_folder, "resultado_extracao.csv")
        self.json_path = os.path.join(self.json_folder, "resultado_extracao.json")

        # Garante que as pastas existam
        os.makedirs(self.csv_folder, exist_ok=True)
        os.makedirs(self.json_folder, exist_ok=True)

    def save_to_csv(self, dataframe):
        """Salva o DataFrame no arquivo CSV na pasta de outputs/csv."""
        if not dataframe.empty:
            # Determina o modo de escrita (append ou write)
            mode = 'a' if os.path.exists(self.csv_path) else 'w'
            header = not os.path.exists(self.csv_path)  # Adiciona cabeçalho apenas na criação

            # Salva o DataFrame no CSV
            dataframe.to_csv(self.csv_path, mode=mode, header=header, index=False)
            print(f"Dados adicionados ao CSV: {self.csv_path}")
        else:
            print("Nenhum dado a salvar no CSV.")

    def save_to_json(self, dataframe):
        """Salva o DataFrame completo em um único arquivo JSON e appenda os novos registros."""
        if not dataframe.empty:
            # Tenta carregar o JSON existente
            if os.path.exists(self.json_path):
                with open(self.json_path, 'r', encoding='utf-8') as json_file:
                    try:
                        existing_data = json.load(json_file)
                    except json.JSONDecodeError:
                        existing_data = []  # Se o arquivo estiver corrompido ou vazio, inicia uma lista vazia
            else:
                existing_data = []

            # Converte o DataFrame para uma lista de dicionários e appenda aos dados existentes
            new_data = dataframe.to_dict(orient="records")
            updated_data = existing_data + new_data

            # Salva o JSON atualizado
            with open(self.json_path, 'w', encoding='utf-8') as json_file:
                json.dump(updated_data, json_file, ensure_ascii=False, indent=4)
            print(f"Dados adicionados ao JSON: {self.json_path}")
        else:
            print("Nenhum dado a salvar no JSON.")