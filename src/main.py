from pdf_decryptor import PDFDecryptor
from pdf_text_extractor import PDFTextExtractor
from pdf_data_extractor import PDFDataExtractor
from pdf_output_handler import PDFOutputHandler


def process_pdfs():
    """
    Pipeline principal para processar PDFs:
    - Descriptografar
    - Extrair texto
    - Extrair dados do texto
    - Salvar outputs em CSV e JSON
    """
    # 1. Descriptografar o primeiro PDF
    decryptor = PDFDecryptor()
    decrypted_pdf_path = decryptor.decrypt_first_pdf()

    # Se não houver PDF descriptografado, encerra o processamento
    if not decrypted_pdf_path:
        print("Nenhum PDF para descriptografar.")
        return

    # 2. Extrair texto de todos os PDFs da pasta decrypted
    extractor = PDFTextExtractor()
    pdfs_text = extractor.extract_text_from_pdfs()

    if not pdfs_text:
        print("Nenhum texto extraído.")
        return

    # 3. Extrair dados do texto usando regex
    data_extractor = PDFDataExtractor()
    df = data_extractor.extract_data(pdfs_text)

    if df.empty:
        print("Nenhum dado extraído do texto.")
        return

    # 4. Gerenciar os outputs (salvar CSV e JSON)
    output_handler = PDFOutputHandler()
    output_handler.save_to_csv(df)
    output_handler.save_to_json(df)

    print("Processamento concluído com sucesso!")


if __name__ == "__main__":
    process_pdfs()