from pdf_decryptor import PDFDecryptor
from pdf_text_extractor import PDFTextExtractor
from pdf_data_extractor import PDFDataExtractor

def main():
    # 1. Descriptografar o primeiro PDF
    decryptor = PDFDecryptor()
    decrypted_pdf_path = decryptor.decrypt_first_pdf()
    
    # Se não houver PDF descriptografado, encerra o processamento
    if not decrypted_pdf_path:
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

    # Exibir o DataFrame ou salvá-lo em CSV
    print(df.head())
    df.to_csv("resultado_extracao.csv", index=False)
    print("Dados extraídos salvos em resultado_extracao.csv")

if __name__ == "__main__":
    main()