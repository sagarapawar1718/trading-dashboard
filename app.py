import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.title("📊 माझे ट्रेडिंग डॅशबोर्ड")
stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "SBIN.NS"]

if st.button("डेटा पहा"):
    data_list = []
    for stock in stocks:
        df = yf.download(stock, period="1mo", interval="1d", progress=False)
        if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
        
        rsi = ta.momentum.rsi(df['Close'], window=14).iloc[-1]
        data_list.append({"Stock": stock, "Price": round(df['Close'].iloc[-1], 2), "RSI": round(rsi, 2)})
    
    st.table(pd.DataFrame(data_list))
    st.success("डेटा अपडेट झाला!")
