### Welcome to Mapa Regex Project 🇵🇹🇵🇹🇵🇹

##### Estrutura do projeto:

project/
    src/
        main.py
        config.py
        pdf_decryptor.py
        pdf_text_extractor.py
        pdf_data_extractor.py
        __init__.py
    maps/
        encrypted/
            # Arquivos PDF criptografados
        decrypted/
            # Arquivos PDF descriptografados
            processed/
                # Arquivos PDF já processados
    requirements.txt
    README.md

#### Projeto de Extração de Dados de Mapa de Responsabilidade PT

##### Instruções
1. Crie o ambiente virtual (opcional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate # Linux/MacOS
   venv\Scripts\activate # Windows


2.	Instale as dependências:
pip install -r requirements.txt


3.	Coloque seus PDFs criptografados em maps/encrypted/.

4.	Rode o script principal: python src/main.py


5.	Os PDFs descriptografados aparecerão em maps/decrypted/. Após a extração do texto, os PDFs serão movidos para maps/decrypted/processed/.

6.	O resultado da extração (CSV) ficará no diretório raiz do projeto, no arquivo resultado_extracao.csv.

---

Com isso, você tem todos os arquivos necessários. Basta copiar o código em arquivos com os nomes correspondentes no seu ambiente local.