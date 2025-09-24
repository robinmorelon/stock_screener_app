

import yfinance as yf
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt




st.title("📊 Evaluation Fair Price")
st.write("Evaluation du prix en fonction de l'augmentation du FCF.")
st.caption("Une approche simple pour estimer la valeur réelle d'une action à partir du Free Cash Flow.")


# Entrée utilisateur
tab1, tab2, tab3 = st.tabs(["⚙️ Paramètres", "📈 Résultats", "📊 Graphique"])
with tab1:
    st.subheader("⚙️ Paramètres d'analyse")
    tickers = st.text_input("Entrez un ticker (ex : AAPL) :", value="AAPL")
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



if tickers:
    dico = calcul_DCF(tickers, hypothese_croissance, price_fcf_attendu)

    with tab2:
        st.subheader("📈 Résultats de l'évaluation")

        col1, col2, col3 = st.columns(3)
        col1.metric("💵 Prix actuel", f"${dico['Prix actuel']}")
        col2.metric("🎯 Fair Price", f"${dico['Fair price']}")
        col3.metric("📈 CACGR (5 ans)", f"{dico['CACGR']}%",
                    delta=f"{dico['CACGR'] - rendement:.2f}%" if dico['CACGR'] else None)

        with st.expander("ℹ️ Explication des résultats"):
            st.markdown("""
                - **Fair Price** : valeur théorique de l’action en fonction du FCF projeté et actualisé.  
                - **CACGR (taux de croissance annuel composé)** : rendement moyen attendu si l’action atteint le prix cible.  
                - **Couleur verte/rouge** : indique si le rendement est supérieur au minimum souhaité.  
                """)

        with tab3:
            st.subheader("📊 Évolution historique et Fair Price")
            periode = st.selectbox("Période :", ["1y", "5y", "10y"], index=1)
            dico = calcul_DCF(tickers, hypothese_croissance, price_fcf_attendu)
            plot(tickers, dico["Fair price"], periode)