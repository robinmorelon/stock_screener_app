

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
    st.subheader('Bénéfices Net', divider="blue")
    tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
    net_income.index = pd.to_datetime(net_income.index).year
    tab1.bar_chart(net_income)
    tab2.write(net_income)

def plot_revenue(revenue):
    st.subheader("Chiffre d'affaires", divider="blue")
    tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
    revenue.index = pd.to_datetime(revenue.index).year
    tab1.bar_chart(revenue)
    tab2.write(revenue)

def plot_free_cashflow(free_cashflow):
    st.subheader("Free Cash Flow", divider="blue")
    tab1, tab2 = st.tabs(["📈 Bar Chart", "🗃 Data"])
    free_cashflow.index = pd.to_datetime(free_cashflow.index).year
    tab1.bar_chart(free_cashflow)
    tab2.write(free_cashflow)

def consensus_color(consensus):
    if consensus == "strongBuy" or consensus == "buy":
        return "green"
    elif consensus == "sell" or consensus == "strongSell":
        return "red"
    else:
        return "gray"

def plot_consensus(ticker):
    stock = yf.Ticker(ticker)
    moyenne_recommendation = stock.get_info()["recommendationKey"]
    st.subheader(f'Consensus : {moyenne_recommendation}', divider=consensus_color(moyenne_recommendation))
    recommendations = stock.get_recommendations().drop("period", axis=1)
    x = recommendations.loc[0].index
    y = recommendations.loc[0].values
    fig, ax = plt.subplots()
    ax.pie(y, labels=x, autopct=lambda t:f"{int(t)}", startangle=90)
    ax.set_title(f"Consensus des analystes pour {ticker}")
    st.pyplot(fig)

def summury(ticker):
    stock = yf.Ticker(ticker)
    st.subheader('À propos', divider="blue")
    st.write(stock.get_info()["longBusinessSummary"])

def converti_milliard(nb):
    nb = str(nb)
    if len(nb)>=10:
        return str(nb[:(len(nb)-9)])+" Mds"
    return str(nb)

def metric(ticker):
    stock = yf.Ticker(ticker)
    pct_change = (stock.info["currentPrice"] * 100 / stock.info["regularMarketPreviousClose"] - 100)
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Prix actuel", value=str(stock.info["currentPrice"])+" "+stock.info["currency"], delta=(str(round(pct_change,2))+"%"))
    col2.metric(label="Capitalisation boursière", value=converti_milliard(stock.info["marketCap"]))
    col3.metric(label="Price/Earning Ratio", value=int(stock.info["trailingPE"]))

def dividend(ticker):
    stock = yf.Ticker(ticker)
    st.subheader('Dividendes', divider="blue")
    if len(stock.dividends)==0:
        st.write("L'entreprise ne verse pas de dividendes")
    else:
        annual_dividends = stock.dividends.resample('Y').sum()
        annual_dividends = annual_dividends.drop(annual_dividends.index[-1])
        annual_dividends = annual_dividends.tail(5)
        payout_ratio = stock.info["payoutRatio"]
        croissance_dividends_5A = (annual_dividends.iloc[-1]*100 / annual_dividends.iloc[0] - 100) / 5
        rendement = stock.info["dividendYield"]
        fig, ax = plt.subplots()
        ax.plot(pd.to_datetime(annual_dividends.index).year, annual_dividends.values, marker='o', linestyle='--')
        ax.set_title('Dividendes')
        ax.set_xticks(pd.to_datetime(annual_dividends.index).year)
        plt.xlabel('Année')
        plt.ylabel('Montant des dividendes')
        st.pyplot(fig)
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Payout Ratio", value=str(round(payout_ratio*100, 2))+" %")
        col2.metric(label="Rendement", value=str(rendement)+" %")
        col3.metric(label="Croissance sur 5 ans", value=str(round(croissance_dividends_5A,2))+" %")

# Interface utilisateur Streamlit
st.title("📊 Screener Boursier Automatisé")
ticker = st.text_input("Entrez un ticker (ex : AAPL) :")
if st.button("Analyser"):
    financial_data, cashflow_data, historical_data = calculate_historical_metrics(ticker)
    metric(ticker)
    summury(ticker)
    plot_revenue(financial_data.loc["Total Revenue"])
    plot_net_income(financial_data.loc["Net Income"])
    plot_free_cashflow(cashflow_data.loc["Free Cash Flow"])
    plot_consensus(ticker)
    dividend(ticker)
