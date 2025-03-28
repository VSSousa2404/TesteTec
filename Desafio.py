from http.client import responses
from importlib.metadata import requires
import pandas as pd
import PyPDF2
import zipfile
import os
import requests
from bs4 import BeautifulSoup

#Anexo 1
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

response = requests.get(url)

caminho = os.path.join("Anexos", "Anexo1.pdf")

with open(caminho,'wb') as f:
    f.write(response.content)
########

#Anexo 2
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

response = requests.get(url)

caminho = os.path.join("Anexos", "Anexo2.pdf")

with open(caminho,'wb') as f:
    f.write(response.content)
#########


with open("Anexos/Anexo1.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    abreviacoes_coluna = {
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial"
    }

data = [line.split() for line in text.split("\n")]

df = pd.DataFrame(data)

df = df.replace(abreviacoes_coluna)

df.to_csv("Teste_Victor.csv", index=False)

Teste_Victor_zip = "Teste_Victor_zip.zip"

with zipfile.ZipFile(Teste_Victor_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("Anexos/Anexo1.pdf", os.path.basename("Anexos/Anexo1.pdf"))
    zipf.write("Anexos/Anexo2.pdf", os.path.basename("Anexos/Anexo2.pdf"))

pastaZip = "Anexos"

anexoZip = os.path.join("Anexos", "AnexosZip")

with zipfile.ZipFile(Teste_Victor_zip, "r") as zipf:
    zipf.extractall("Anexos")