


import streamlit as st

st.title('InvestMate')
st.write("Bienvenue sur ma plateforme dédiée à l'analyse des actions et à l'évaluation du prix juste d'une action en bourse. Ce site vous permet d'explorer les performances financières d'une société, ainsi que d'évaluer son Fair Price en fonction de ses flux de trésorerie futurs.")

pages = {"Stock screener": [st.Page("screener_python.py")], "Evaluation du prix juste": [st.Page("fair_price.py")]}
pg = st.navigation(pages)
pg.run()