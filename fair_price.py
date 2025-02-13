

import yfinance as yf
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt




st.title("📊 Evaluation Fair Price")
st.write("Evaluation du prix en fonction de l'augmentation du FCF.")

# Entrée utilisateur
tickers = st.text_input("Entrez un ticker (ex : AAPL) :")


hypothese_croissance = st.slider("Entrez l'hypothèse de croissance (ex : 20) : ",0,100)



price_fcf_attendu = st.slider("Entrez le P/FCF attendu : ",0,100)


rendement = st.slider("Entrez le rendement minimum souhaité (12 par défaut) :", value=12)

def calcul_DCF(ticker, hypothese_croissance, price_fcf_attendu):
    stock = yf.Ticker(ticker)
    free_cash_flow = stock.cashflow.T["Free Cash Flow"]
    shares = stock.info['sharesOutstanding']
    fcf_by_share = free_cash_flow.iloc[0] / shares
    fcf_first_year = fcf_by_share * (1 + (hypothese_croissance / 100))
    fcf_second_year = fcf_first_year * (1 + (hypothese_croissance / 100))
    fcf_third_year = fcf_second_year * (1 + (hypothese_croissance / 100))
    fcf_fourth_year = fcf_third_year * (1 + (hypothese_croissance / 100))
    fcf_fifth_year = fcf_fourth_year * (1 + (hypothese_croissance / 100))
    current_price = stock.info['currentPrice']
    final_price = fcf_fifth_year * price_fcf_attendu
    CACGR = (((final_price / current_price) ** (1 / 5)) - 1) * 100
    fair_price = final_price / ((1 + 0.12) ** 5)
    dico = {"Ticker": ticker, "Free Cash Flow par action": round(fcf_by_share, 2), "Prix actuel": current_price,
            "Prix final": round(final_price, 2), "Fair price": round(fair_price, 2), "CACGR": round(CACGR, 2)}
    return dico

def plot(ticker, fair_price, periode="10y"):
    stock = yf.Ticker(ticker)
    stock_history = stock.history(period=periode, interval="1wk")
    stock_history = stock_history.reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(stock_history['Date'], stock_history['Open'], label="Prix d'ouverture", color="blue")
    ax.axhline(y=fair_price, color="red", linestyle="--", label=f"Prix juste = {fair_price}")
    ax.set_title(f"Historique des prix de l'action {ticker}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Prix")
    ax.legend()
    st.pyplot(fig)



if st.button("Calculate fair price"):
    dico = calcul_DCF(tickers, hypothese_croissance, price_fcf_attendu)
    df = pd.DataFrame([dico])
    def color_CACGR(x):
        if x >= rendement:
            return "background-color: green;"
        else:
            return "background-color: red;"
    styled_df = df.style.format(precision=2).applymap(color_CACGR, subset=["CACGR"])
    st.dataframe(styled_df,hide_index=True, width=800)
    #plot(tickers, dico["Fair price"])
    st.session_state["periode"] = "10y"

if "periode" in st.session_state:
    periode = st.selectbox("Changez la période du graphique :",("10y", "5y", "1y"))
    if periode:
        dico = calcul_DCF(tickers, hypothese_croissance, price_fcf_attendu)
        plot(tickers, dico["Fair price"], periode)