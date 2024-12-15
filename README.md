# **Mapa Regex Project** 🇵🇹🇵🇹🇵🇹

Bem-vindo ao **Mapa Regex Project**! Este projeto foi desenvolvido para automatizar a extração de dados de PDFs criptografados de mapas de responsabilidade, utilizando técnicas de regex e processamento de texto. É uma solução prática e eficiente para lidar com grandes volumes de documentos PDF protegidos.

---

## **📂 Estrutura do Projeto**

A organização dos arquivos:

project/
│
├── src/
│   ├── main.py              # Script principal para execução do projeto
│   ├── config.py            # Configurações gerais
│   ├── pdf_decryptor.py     # Módulo para descriptografia de PDFs
│   ├── pdf_text_extractor.py# Módulo para extração de texto dos PDFs
│   ├── pdf_data_extractor.py# Módulo para extração de dados formatados usando regex
│   └── __init__.py          # Arquivo de inicialização do pacote
│
├── maps/
│   ├── encrypted/           # Diretório para os PDFs criptografados
│   ├── decrypted/           # Diretório para os PDFs descriptografados
│   │   └── processed/       # PDFs já processados
│
├── requirements.txt         # Arquivo com as dependências do projeto
├── README.md                # Este arquivo
└── resultado_extracao.csv   # Resultado final da extração (gerado pelo script)

---
## **🎯 Objetivo do Projeto**
Este projeto foi criado com o propósito de:
	•	Automatizar a descriptografia de PDFs protegidos por senha.
	•	Extrair textos desses PDFs de forma estruturada.
	•	Processar os dados extraídos utilizando expressões regulares.
	•	Gerar um arquivo CSV consolidado com os dados processados.
---

## **🔮 How to Deploy**

### 1. Configuração do Ambiente

Crie e ative um ambiente virtual (opcional, mas recomendado):

#### Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
```bash
python3 -m venv venv
venv\Scripts\activate
```

2. Instale as Dependências

Após ativar o ambiente virtual, instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

3. Organize os PDFs
Coloque os arquivos PDF criptografados no diretório maps/encrypted/.

4. Execute o Script Principal
Rode o script principal para iniciar o processamento:
python **src/main.py**

5. Resultado do Processamento
	•	Os PDFs descriptografados estarão no diretório **maps/decrypted/.**
	•	PDFs já processados serão movidos para maps/decrypted/processed/.
	•	O arquivo resultado_extracao.csv será gerado no diretório raiz do projeto, contendo os dados extraídos.


🛠️ Tecnologias Utilizadas
	•	Python 3.8+
	•	Bibliotecas:
        •	PyPDF2
        •	re (Regex)
        •	pandas
