from dataclasses import asdict
import dadosCliente
from interface.cliente_modal import Cliente, Bancario
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
    # 1. Descriptografar os PDFs com progresso
    decryptor = PDFDecryptor()
    decrypted_pdfs = decryptor.decrypt_pdfs_with_progress()

    if not decrypted_pdfs:
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
    cliente = Cliente(
        nome="Renan",
        nif="123456789",
        bancario=[
            Bancario(
                mesMapa="Janeiro",
                instituicao="Banco de Portugal",
                divida=500.00,
                parcela="Não",
                garantias=519.90,
                num_devedores=2,
                prod_financeiro="Banco Europeu",
                entrada_incumpr="None",
                data_inicio="2009-05-05",
                data_fim="2010-05-05"
            )
        ]
    )
    
    dadosCliente.extraiDadosCliente(cliente)

    # process_pdfs()