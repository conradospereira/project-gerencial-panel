import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

st.set_page_config(layout="wide")

# Configurar o acesso ao Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(".streamlit/google-sheets-credentials.json", scope)
client = gspread.authorize(creds)

# Abrir a planilha pelo nome
spreadsheet = client.open("Tabela de preço")  # Substitua pelo nome da sua planilha

# Selecionar uma aba específica (substitua 'Nome da Guia' pelo nome da aba desejada)
worksheet = spreadsheet.worksheet('BD')

# Ler os dados da aba específica
data = worksheet.get_all_records()

df = pd.DataFrame(data, columns=['CODIGO INTERNO', 'GTIN', 'REFERENCIA', 'DESCRICAO', 'DEPARTAMENTO', 'GESTOR', 'COD FORNECEDOR', 'DESCRICAO FORNECEDOR', 'PRECO DE COMPRA'])
#df['CODIGO INTERNO'] = pd.to_numeric(df['CODIGO INTERNO'].str.replace(',',''), errors='coerce')

# Exibir os dados na aplicação Streamlit
st.dataframe(df, width=1200)
