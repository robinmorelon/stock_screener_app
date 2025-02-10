
# 📊 **InvestMate** - Plateforme d'Analyse Boursière et Évaluation de Prix Juste

Bienvenue sur **InvestMate**, une application interactive conçue pour faciliter l'analyse des actions et l'évaluation de leur prix juste. Grâce à des données financières en temps réel et des visualisations intuitives, cette plateforme offre un outil puissant pour les investisseurs souhaitant prendre des décisions éclairées.

---

## 🚀 **Fonctionnalités principales**

### 1️⃣ **Stock Screener**
Une interface dédiée à l'analyse rapide et détaillée des performances financières des entreprises.
- **Résumé de l'entreprise** : Description complète de l'activité de la société.
- **Graphiques interactifs** :
  - **Revenus** : Analyse de l'évolution des chiffres d'affaires.
  - **Bénéfices nets** : Visualisation des profits réalisés.
  - **Flux de trésorerie libre (FCF)** : Données sur les liquidités disponibles.
- **Consensus des analystes** :
  - Recommandations affichées sous forme de graphique circulaire.
  - Moyenne des recommandations colorée selon l'avis (achat, vente, etc.).
- **Indicateurs clés** :
  - Prix actuel, capitalisation boursière, ratio P/E, et variation quotidienne.

### 2️⃣ **Évaluation Fair Price**
Une interface dédiée au calcul du prix juste d'une action à l'aide de la méthode Discounted Cash Flow (DCF).
- **Personnalisation des hypothèses** :
  - Taux de croissance estimé pour les flux de trésorerie.
  - Ratio Prix/FCF attendu.
  - Rendement minimum souhaité.
- **Visualisation des résultats** :
  - Tableau interactif avec des couleurs conditionnelles pour le CACGR.
  - Graphique montrant l'évolution des prix historiques avec une ligne représentant le prix juste.
- **Comparaison des périodes** :
  - Sélection dynamique de la période (1 an, 5 ans, 10 ans).

---

## 📋 **Prérequis**

Avant de commencer, assurez-vous que votre environnement est configuré avec les dépendances suivantes :

### **Installation des dépendances**
- Python 3.8 ou supérieur.
- Bibliothèques nécessaires :
  ```bash
  pip install yfinance pandas streamlit matplotlib numpy
  ```

---

## 🧩 **Structure du projet**

- **`main.py`** : Page principale de l'application. Gère la navigation entre les sections.
- **`screener_python.py`** : Logique et interface pour le Stock Screener.
- **`fair_price.py`** : Calcul du Fair Price et interface dédiée.

---

## 🖥️ **Utilisation**

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/[votre-utilisateur]/InvestMate.git
   cd InvestMate
   ```

2. Lancez l'application Streamlit :
   ```bash
   streamlit run main.py
   ```

3. Explorez les sections interactives :
   - **Stock Screener** : Analyse financière détaillée.
   - **Évaluation Fair Price** : Calculez et comparez le prix juste.


---

## 🔧 **Technologies utilisées**

- **Python** : Manipulation des données et calculs financiers.
- **Streamlit** : Interface utilisateur interactive et intuitive.
- **Pandas** : Traitement des données financières.
- **Matplotlib** : Visualisation des graphiques.
- **yfinance** : Extraction des données financières en temps réel.

---

## ✨ **Idées d'amélioration**

- Ajout d'une section dédiée aux dividendes.
- Ajout de prédictions sur les revenus ou bénéfices avec des modèles de régression.
- Intégration d'autres indicateurs financiers comme le ROE ou le PEG ratio.

---

## 🤝 **Contribuer**

Les contributions sont les bienvenues ! Si vous souhaitez signaler un problème ou proposer une fonctionnalité, ouvrez une issue ou soumettez une pull request.


