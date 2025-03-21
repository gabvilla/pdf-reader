import tabula
import pandas as pd

def extract_tables_from_pdf(pdf_path, excel_path):
    # Extrair tabelas do PDF
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    
    # Lista para armazenar tabelas formatadas
    formatted_tables = []
    
    for table in tables:
        # Remover colunas e linhas completamente vazias
        #table = table.dropna(how='all', axis=1)
        #table = table.dropna(how='all', axis=0)
        
        # Ajustar nomes de colunas
        table.columns = [str(col).strip() for col in table.columns]
        
        # Filtrar apenas colunas relevantes (ajustar conforme necessário)
        expected_columns = ["CPF/CNPJ", "Nome/Nome Social/Razão Social", "Ativ./Tipo(E/S)", "No NF", "Emissão da NF", "Qtd(Kg)", "Qtd(L)"]
        table = table[[col for col in table.columns if col in expected_columns]]
        
        # Adicionar tabela formatada à lista
        formatted_tables.append(table)

    # Concatenar todas as tabelas em um único DataFrame
    df = pd.concat(formatted_tables, ignore_index=True)
    
    # Salvar em uma única sheet do Excel
    df.to_excel(excel_path, sheet_name='Dados Extraídos', index=False, engine='openpyxl')
    
    print(f"Arquivo Excel salvo em: {excel_path}")

# Caminho do arquivo PDF e do Excel
pdf_file = "relatorio_irregularidade - 2025-02-25T144256.934.pdf"
excel_file = "saida.xlsx"
extract_tables_from_pdf(pdf_file, excel_file)


