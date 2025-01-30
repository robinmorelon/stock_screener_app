

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
    st.subheader('Bénéfices Net')
    tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
    net_income.index = pd.to_datetime(net_income.index).year
    tab1.bar_chart(net_income)
    tab2.write(net_income)

def plot_revenue(revenue):
    st.subheader("Chiffre d'affaires")
    tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
    revenue.index = pd.to_datetime(revenue.index).year
    tab1.bar_chart(revenue)
    tab2.write(revenue)

def plot_free_cashflow(free_cashflow):
    st.subheader("Free Cash Flow")
    tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
    free_cashflow.index = pd.to_datetime(free_cashflow.index).year
    tab1.bar_chart(free_cashflow)
    tab2.write(free_cashflow)

def plot_consensus(ticker):
    stock = yf.Ticker(ticker)
    st.subheader('Consensus')
    recommendations = stock.get_recommendations().drop("period", axis=1)
    x = recommendations.loc[0].index
    y = recommendations.loc[0].values
    fig, ax = plt.subplots()
    ax.pie(y, labels=x, autopct=lambda t:f"{int(t)}", startangle=90)
    ax.set_title(f"Consensus des analystes pour {ticker}")
    st.pyplot(fig)


# Interface utilisateur Streamlit
st.title("📊 Screener Boursier Automatisé")
ticker = st.text_input("Entrez un ticker (ex : AAPL) :")
if st.button("Analyser"):
    financial_data, cashflow_data, historical_data = calculate_historical_metrics(ticker)
    plot_revenue(financial_data.loc["Total Revenue"])
    plot_net_income(financial_data.loc["Net Income"])
    plot_free_cashflow(cashflow_data.loc["Free Cash Flow"])
    plot_consensus(ticker)