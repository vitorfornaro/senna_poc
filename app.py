import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader  # Certifique-se de instalar: pip install PyPDF2

# Função para processar o PDF e extrair texto
def process_pdf(uploaded_file):
    try:
        pdf_reader = PdfReader(uploaded_file)
        full_text = ""
        for page in pdf_reader.pages:
            full_text += page.extract_text()
        return full_text
    except Exception as e:
        st.error(f"Erro ao processar o PDF: {e}")
        return None

# Função para extrair dados do texto (exemplo fictício de extração de tabelas)
def extract_data_from_text(full_text):
    try:
        # Simulação de dados extraídos
        data = {
            "Tarefa": ["Planejamento", "Execução", "Revisão"],
            "Responsável": ["Maria", "João", "Ana"],
            "Prazo": ["2024-12-31", "2025-01-15", "2025-02-01"]
        }
        df = pd.DataFrame(data)  # Simulação para fins de teste
        return df
    except Exception as e:
        st.error(f"Erro ao extrair dados do texto: {e}")
        return pd.DataFrame()

# Interface do Streamlit
st.title("Processador de Mapas de Responsabilidade")
uploaded_file = st.file_uploader("Carregue um arquivo PDF", type="pdf")

if uploaded_file is not None:
    st.info("Processando o PDF...")
    full_text = process_pdf(uploaded_file)
    if full_text:
        st.success("Texto extraído com sucesso!")
        st.text("Visualizando as primeiras páginas:")
        st.text(full_text[:1000])  # Exibir os primeiros 1000 caracteres

        st.info("Extraindo dados do texto...")
        df = extract_data_from_text(full_text)
        if not df.empty:
            st.success("Dados extraídos com sucesso!")
            st.dataframe(df.tail())  # Mostrar as últimas linhas do DataFrame
        else:
            st.warning("Nenhum dado relevante foi encontrado no PDF.")