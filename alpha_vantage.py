import pandas as pd
import requests, os
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv as env

env()

@st.cache_data
def busca_acoes(base_url, symbol):
    parameters = {'function': 'SYMBOL_SEARCH', 'keywords': symbol}
    response = requests.get(base_url, params=parameters)
    data = response.json()
    return data


@st.cache_data
def pegar_ativo(nome_do_ativo, base_url):
    parameters = {'function': 'TIME_SERIES_MONTHLY', 'symbol': nome_do_ativo}
    response = requests.get(base_url, params=parameters)
    data_frame = response.json()
    return data_frame


st.title('Stock Dashboard')
API_key = os.getenv('API_KEY')
base_url = f'https://www.alphavantage.co/query?&apikey={API_key}'

symbol = st.sidebar.text_input('Ticker name')
if symbol:
    data = busca_acoes(base_url=base_url, symbol=symbol)
    if 'bestMatches' in data:
        stock_options = [f"{match['1. symbol']} - {match['2. name']}" for match in data["bestMatches"]]
        escolha_sua_acao = st.sidebar.selectbox('Ticker selection', stock_options)
        
        if escolha_sua_acao:
            symbol_ativo = escolha_sua_acao.split(' - ')[0]
            nome_acao = escolha_sua_acao.split(' - ')[1]
            ativo = pegar_ativo(symbol_ativo, base_url)
            df = pd.DataFrame.from_dict(ativo['Monthly Time Series'], orient='index').reset_index()
            df.columns = ['Date', 'Opening', 'High', 'Low', 'Closing', 'Volume']
            df['Date'] = pd.to_datetime(df['Date'])
            df['Closing'] = df['Closing'].astype(float)
            start_date = pd.to_datetime(st.sidebar.date_input('Start Date',
                                                              value=df['Date'].min(), 
                                                              min_value=df['Date'].min(),
                                                              max_value=df['Date'].max()))
            end_date = pd.to_datetime(st.sidebar.date_input('End Date',
                                                            value=df['Date'].max(),
                                                            min_value=df['Date'].min(),
                                                            max_value=df['Date'].max()))
            date_choosen_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
            fig = px.line(date_choosen_df, x='Date', y='Closing', title=nome_acao)
            st.plotly_chart(fig)

