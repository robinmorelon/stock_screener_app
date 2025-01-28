

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def calculate_historical_metrics(ticker):
    stock = yf.Ticker(ticker)
    financial_data = stock.financials
    cashflow_data = stock.cashflow
    historical_data = stock.history(period='5y')
    return financial_data, cashflow_data, historical_data

def plot_net_income(net_income):
    net_income.index = pd.to_datetime(net_income.index).year
    st.write("Bénéfices Net")
    st.bar_chart(net_income)

def plot_revenue(revenue):
    revenue.index = pd.to_datetime(revenue.index).year
    st.write("Chiffre d'affaires")
    st.bar_chart(revenue)

def plot_free_cashflow(free_cashflow):
    free_cashflow.index = pd.to_datetime(free_cashflow.index).year
    st.write("Free Cashflow")
    st.bar_chart(free_cashflow)

# Interface utilisateur Streamlit
st.title("📊 Screener Boursier Automatisé")
ticker = st.text_input("Entrez un ticker (ex : AAPL) :")
if st.button("Analyser"):
    financial_data, cashflow_data, historical_data = calculate_historical_metrics(ticker)
    plot_revenue(financial_data.loc["Total Revenue"])
    plot_net_income(financial_data.loc["Net Income"])
    plot_free_cashflow(cashflow_data.loc["Free Cash Flow"])