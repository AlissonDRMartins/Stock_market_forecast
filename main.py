import pandas as pd, streamlit as st, plotly.express as px, requests, os
from prophet import Prophet
from prophet.plot import plot_plotly
from dotenv import load_dotenv as env


@st.cache_data
def search_stocks(base_url, symbol):
    parameters = {'function': 'SYMBOL_SEARCH', 'keywords': symbol}
    response = requests.get(base_url, params=parameters)
    data = response.json()
    return data


@st.cache_data
def get_ticker(ticker_name, base_url):
    parameters = {'function': 'TIME_SERIES_MONTHLY', 'symbol': ticker_name}
    response = requests.get(base_url, params=parameters)
    data_frame = response.json()
    return data_frame


env()
st.title('Stock Market Project')
st.header('Overview of Stock')
API_key = os.getenv('API_KEY')
base_url = f'https://www.alphavantage.co/query?&apikey={API_key}'
symbol = st.sidebar.text_input('Ticker name')
tab1, tab2 = st.tabs(['Stock View', 'Stock Prediction'])

if symbol:
    data = search_stocks(base_url=base_url, symbol=symbol)

    if 'bestMatches' in data:
        stock_options = [f"{match['1. symbol']} - {match['2. name']}" for match in data["bestMatches"]]
        escolha_sua_acao = st.sidebar.selectbox('Ticker selection', stock_options)
        
        if escolha_sua_acao:
            symbol_ativo = escolha_sua_acao.split(' - ')[0]
            nome_acao = escolha_sua_acao.split(' - ')[1]
            ativo = get_ticker(symbol_ativo, base_url)
            with tab1:
                st.markdown("""
                    ### Stock Closing Prices Over Time
                    This chart illustrates the monthly closing prices of the selected stock. Key insights include:
                    - **Trend Analysis:** Observe the overall trend of the stock prices over the selected period.
                    - **Volatility:** Identify periods of high volatility through significant ups and downs in the chart.
                    - **Historical Performance:** Assess the stock's performance over a long time frame.
                    
                    Use the date selectors in the sidebar to customize the time range.
                """)   
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

            with tab2:

                df_pred = df[['Date', 'Closing']]
                df_pred = df_pred.rename(columns={'Date': 'ds', 'Closing': 'y'})
                fbp = Prophet(daily_seasonality=True, interval_width=0.95)
                fbp.fit(df_pred)
                fut = fbp.make_future_dataframe(periods=30, freq='M')
                st.markdown("""
                            ### Forecast Chart
                            - **Black dots:** Actual observed values
                            - **Light blue area:** Uncertainty interval
                            - **Dark blue line:** Forecasted values

                            Use the date range below the main graph to select a period.
                            """)
                forecast = fbp.predict(fut)
                fig = plot_plotly(fbp, forecast, xlabel='Date', ylabel='Value')
                st.plotly_chart(fig)

