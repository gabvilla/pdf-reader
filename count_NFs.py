import pdfplumber
import re
import pandas as pd

def contar_nfs (pdf_path):
   nfs = []

   nf_pattern = re.compile(r'\b\d{4,7}\b')
   nf_header = "NF"

   with pdfplumber.open(pdf_path) as pdf:
      for page in pdf.pages:
        text = page.extract_text()
        lines = text.split("\n")
        for line in lines:
           print(lines.index(line + 1))
        

      """ if text:
      matches = nf_pattern.findall(text)
      nfs.update(matches) """
   

   print(f"Total de NFs encontradas: {len(nfs)}")
"""    df = pd.DataFrame(nfs)
   df.to_excel("NFs.xlsx", sheet_name='NFs', index=False, engine='openpyxl') """


   #return nfs


pdf_file = "relatorio_irregularidade - 2025-02-25T144256.934.pdf"
contar_nfs(pdf_file)