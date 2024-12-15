import streamlit as st
import pandas as pd
import plotly.graph_objects as go



# Configuration de la page Streamlit
st.set_page_config( layout="wide")  # page_title="Application avec fond global"

# Application du fond pour toute l'application (CSS)
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;  /* Couleur de fond de la page */
            font-family: 'Arial', sans-serif;  /* Police pour toute l'application */
        }

        .stApp {
            background-color: #f0f8ff;  /* Couleur de fond pour l'ensemble de l'application */
        }

        /* Styles supplémentaires pour certains éléments */
        h1 {
            color: #2c3e50;  /* Couleur des titres */
        }
        .stButton>button {
            background-color: #3498db;  /* Couleur des boutons */
            color: white;  /* Couleur du texte des boutons */
        }
    </style>
""", unsafe_allow_html=True)



# Ajout d'une  page (avec un changement de contenu)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisissez une page", ("Data Management", "Evolution of commodity prices", "Growth Rates of Commodity Prices", "Trading volume", "Volatilité des prix", "Сorrélations des prix de matières premières"))

if page == "Data Management":
    import streamlit as st

    # Titre principal de l'application
    # Le titre s'affiche en haut de la page et donne une vue d'ensemble du sujet.
    st.title("Analyse des Commodities Futures")

    # Ajout d'une information sur le projet avec une date clé
    # Ce texte indique le contexte du projet et sa date importante.
    st.markdown("**Projet data management Paris Sorbonne: 15/12/2024**")

    # Texte explicatif sur les commodities futures
    # Ce bloc de texte explique ce que sont les contrats de futures et leur rôle sur les marchés financiers.
    st.markdown("""
    Les commodities futures sont des contrats financiers permettant d’acheter ou de vendre des matières premières 
    (énergie, métaux, produits agricoles, etc...) à un prix fixé pour une date future.  
    Ils sont utilisés pour se couvrir contre les fluctuations de prix ou pour spéculer.  
    Ces contrats incluent des données clés comme le type de matière, le prix à terme, la date d'échéance,  
    le volume d'échange et la volatilité.  
    Ils jouent un rôle central dans la gestion des risques et l’analyse des tendances des marchés mondiaux.
    """)

    # Section détaillée sur le projet
    # Ce bloc décrit les étapes clés du projet, organisé en deux phases : gestion des données et visualisation.
    st.markdown("""
    ### Project_

    This project is part of the Data Analytics Paris Sorbonne diploma, with a focus on data management and data visualization.

          (1) The first step is the data management phase, carried out on jupyter_notebook with Pandas : 

                  - Analysis and cleaning of the dataset: Commodities-Futures-Collection

                  - Data export for visualization and analysis.

          (2) The second step is the data visualization phase, performed on the exported data:

                  - Statistical calculations and trend visualization with Numpy, Scipy, Matplot.
    """)

    st.header("Description du Jeu de Données")

    import streamlit as st
    import pandas as pd

    st.markdown(
        "Origine des données : [https://www.kaggle.com/datasets/guillemservera/commodities-futures-collection](https://www.kaggle.com/datasets/guillemservera/commodities-futures-collection)")

    import streamlit as st
    import pandas as pd

    import streamlit as st
    import pandas as pd

    # Description des colonnes
    columns_description = {
        "date": "La date associée à l'enregistrement des marchandises.",
        "commodity": "Le nom de la marchandise (ex. : pétrole, or, blé) associée à cet enregistrement.",
        "ticker": "Le symbole ou identifiant unique utilisé pour représenter la marchandise sur les marchés financiers.",
        "category": "La classification de la marchandise (par exemple : énergie, métaux précieux, agriculture).",
        "open": "Le prix d'ouverture de la marchandise pour la période indiquée dans la colonne date.",
        "high": "Le prix le plus élevé atteint par la marchandise pendant la période indiquée.",
        "low": "Le prix le plus bas atteint par la marchandise pendant la période indiquée.",
        "close": "Le prix de clôture de la marchandise pour la période indiquée.",
        "volume": "Le volume total échangé pour la marchandise pendant la période indiquée.",
    }

    # Conversion du dictionnaire en DataFrame pour l'afficher sous forme de tableau
    description_df = pd.DataFrame(
        list(columns_description.items()),  # Transformation des éléments du dictionnaire en liste
        columns=["Colonne", "Description"]  # Noms des colonnes dans le tableau
    )

    # Suppression de la première colonne contenant les indices (qui est par défaut dans une DataFrame)
    description_df.reset_index(drop=True, inplace=True)

    # Affichage du titre sans gras et avec une taille de police plus petite
    st.markdown("<h3 style='font-weight: normal;'>Description des colonnes</h3>", unsafe_allow_html=True)

    # Affichage du tableau sans la colonne d'index
    st.table(description_df)  # Affiche la table sans la colonne d'index



    st.write("Il y a 135295 observations et 9 variables dans le jeu de données.")

    types_data = {
        "ticker": "category",  # Type 'category' pour la variable ticker
        "category": "category",  # Type 'category' pour la variable category
        "commodity": "category",  # Type 'category' pour la variable commodity
        "date": "datetime64[ns]",  # Type 'datetime64[ns]' pour la variable date
        "open": "float64",  # Type 'float64' pour la variable open
        "high": "float64",  # Type 'float64' pour la variable high
        "low": "float64",  # Type 'float64' pour la variable low
        "close": "float64",  # Type 'float64' pour la variable close
        "volume": "int64"  # Type 'int64' pour la variable volume
    }

    # Conversion des données en DataFrame pour l'affichage sous forme de tableau
    types_df = pd.DataFrame(list(types_data.items()), columns=["Variable", "Type"])

    # Affichage du titre
    st.write("Types de variables:")

    # Affichage du tableau avec les types de variables
    st.table(types_df)

    st.write("Il n'y a ni valeurs manquantes ni doublons à première vue, mais toutes les marchandises ne se trouvent pas dans la même plage de dates. Déterminerons les vraies valeurs manquantes en utilisant la même plage de dates pour toutes les matières premières.")

    import streamlit as st
    import pandas as pd

    # Данные о товарах и их значениях
    commodity_data = {
        "Commodity": [
            "Brent Crude Oil", "Cocoa", "Coffee", "Copper", "Corn", "Cotton",
            "Crude Oil", "Gold", "Heating Oil", "KC HRW Wheat", "Lean Hogs",
            "Live Cattle", "Natural Gas", "Oat", "Orange Juice", "Palladium",
            "Platinum", "RBOB Gasoline", "Random Length Lumber", "Rough Rice",
            "Silver", "Soybean", "Soybean Oil", "Sugar"
        ],
        "Nombre de valeurs NA": [
            1977, 36, 39, 194, 186, 37, 189, 198, 196, 197, 570, 584, 193,
            207, 5469, 490, 730, 235, 450, 43, 197, 194, 170, 76
        ],
        "Pourcentage de valeurs NA": [
            32.0, 0.6, 0.6, 3.1, 3.0, 0.6, 3.1, 3.2, 3.2, 3.2, 9.2, 9.5, 3.1,
            3.4, 88.6, 7.9, 11.8, 3.8, 7.3, 0.7, 3.2, 3.1, 2.8, 1.2
        ]
    }

    # Создание DataFrame из данных
    commodity_df = pd.DataFrame(commodity_data)

    # Отображение таблицы в Streamlit
    st.write("Nombre et pourcentage de valeurs NA:")
    st.table(commodity_df)

    gestion_na = {
        "Type de gestion des NA": [
            "Ajout des données provenant de la source (Yahoo Finance) si elles sont disponibles",
            "Suppression des données avec un pourcentage très élevé de valeurs NA",
            "Remplissage des valeurs nulles par propagation vers l'avant (ffill)"

        ],
        "Matières premières concernées": [
            "Lean Hogs, Live Cattle, Orange Juice, Oat, Soybean Oil",
            "Brent Crude Oil, Palladium, Platinum, Random Length Lumber",
            "Tous les autres matières premières"

        ]
    }

    # Создание DataFrame из данных
    df_gestion_na = pd.DataFrame(gestion_na)

    # Отображение таблицы в Streamlit
    st.write("Type de gestion des valeurs manquantes appliqué:")
    st.table(df_gestion_na)

    df_complet = pd.read_csv('df_complet.csv')

    # Affichage des premières lignes des données
    st.write("Aperçu des données :", df_complet.head())

    # Affichage des statistiques descriptives
    st.write("Statistiques descriptives :")
    st.write(df_complet.describe())





if page == "Evolution of commodity prices":
    #   import streamlit as st
    #   import pandas as pd
    #   import plotly.graph_objects as go

    # Titre de la deuxième page
    st.title("Evolution of commodity prices")

    # Charger les données
    df = pd.read_csv('df_complet.csv')

    # Création d'une mise en page avec deux colonnes
    col1, col2 = st.columns([2, 5])  # Largeur relative : 1 pour les widgets, 4 pour le graphique

    # Colonne de gauche : filtres
    with col1:
        # Filtre par catégorie
        categories = df["category"].unique()
        selected_category = st.selectbox(
            "Choisissez une catégorie :", categories
        )

        # Filtre par produit (basé sur la catégorie sélectionnée)
        filtered_by_category = df[df["category"] == selected_category]
        commodities = filtered_by_category["commodity"].unique()
        selected_commodities = st.multiselect(
            "Choisissez les produits à afficher :",
            commodities,
            default=commodities
        )

    # Filtrer les données en fonction des choix
    filtered_df = filtered_by_category[filtered_by_category["commodity"].isin(selected_commodities)]

    # Création du graphique linéaire
    fig = go.Figure()

    # Ajouter une trace par produit sélectionné
    for commodity in selected_commodities:
        commodity_data = filtered_df[filtered_df["commodity"] == commodity]
        fig.add_trace(
            go.Scatter(
                x=commodity_data["date"],
                y=commodity_data["close"],  # Utiliser le prix de clôture pour le graphique linéaire
                mode='lines',  # Mode "lines" pour le graphique linéaire
                name=commodity
            )
        )

    # Configuration du graphique
    fig.update_layout(
        title="Evolution des prix des matières premières",
        xaxis_title="Date",
        yaxis_title="Prix",
        xaxis_rangeslider_visible=False,
        paper_bgcolor='rgba(0,0,0,0)',  # Fond autour du graphique transparent
        plot_bgcolor='rgba(0,0,0,0)',  # Fond de la zone de traçage transparent
    )

    # Colonne de droite : affichage du graphique
    with col2:
        st.plotly_chart(fig)




if page == "Growth Rates of Commodity Prices":

    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go

    # Titre de la page
    st.title("Growth Rates of Commodity Prices")

    # Charger les données
    df = pd.read_csv('df_complet.csv')

    # Convertir la colonne 'date' en type datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    # Trouver la date maximale dans les données
    max_date = df['date'].max()

    # Créer une mise en page avec deux colonnes
    col1, col2 = st.columns([2, 5])  # Largeur relative : 2 pour les widgets, 5 pour le graphique

    # Colonne de gauche : filtres
    with col1:
        # Filtre par catégorie
        categories = df["category"].unique()
        selected_category = st.selectbox(
            "Choisissez une catégorie :", categories
        )

        # Filtre par produit (basé sur la catégorie sélectionnée)
        filtered_by_category = df[df["category"] == selected_category]
        commodities = filtered_by_category["commodity"].unique()
        selected_commodities = st.multiselect(
            "Choisissez les produits à afficher :",
            commodities,
            default=commodities
        )

        # Sélection de la fréquence (Année ou Trimestre)
        frequency = st.radio(
            "Choisissez la fréquence :",
            options=["Année", "Trimestre"]
        )

        # Définir les dates en fonction de la fréquence choisie
        if frequency == "Année":
            # Si la fréquence est "Année", la date de début est 01.01.2002 et la date de fin est 31.12.2023
            start_date = st.date_input(
                "Choisissez la date de début :",
                value=pd.to_datetime("2002-01-01"),
                min_value=pd.to_datetime("2002-01-01"),
                max_value=pd.to_datetime("2023-12-31")
            )
            end_date = st.date_input(
                "Choisissez la date de fin :",
                value=pd.to_datetime("2023-12-31"),
                min_value=start_date,
                max_value=pd.to_datetime("2023-12-31")
            )
        elif frequency == "Trimestre":
            # Si la fréquence est "Trimestre", la date de début est 01.10.2001
            start_date = st.date_input(
                "Choisissez la date de début :",
                value=pd.to_datetime("2001-10-01"),
                min_value=pd.to_datetime("2001-10-01"),
                max_value=max_date  # Utilisation de max_date ici
            )
            end_date = st.date_input(
                "Choisissez la date de fin :",
                value=max_date,  # La date de fin est la date maximale dans les données
                min_value=start_date,
                max_value=max_date
            )

    # Filtrer les données en fonction des choix de l'utilisateur
    filtered_df = filtered_by_category[filtered_by_category["commodity"].isin(selected_commodities)]
    filtered_df = filtered_df[
        (filtered_df["date"] >= pd.Timestamp(start_date)) & (filtered_df["date"] <= pd.Timestamp(end_date))]

    # Calculer le taux de croissance annuel
    filtered_df["year"] = filtered_df["date"].dt.year
    filtered_df = filtered_df.sort_values(by=["commodity", "year"])

    # Calculer le taux de croissance selon la fréquence choisie (Année ou Trimestre)
    if frequency == "Année":
        annual_growth = filtered_df.groupby(["commodity", "year"])["close"].last().pct_change() * 100
    elif frequency == "Trimestre":
        # Ajouter la colonne 'quarter' pour les trimestres
        filtered_df["quarter"] = filtered_df["date"].dt.to_period("Q")
        quarterly_growth = filtered_df.groupby(["commodity", "quarter"])["close"].last().pct_change() * 100
        annual_growth = quarterly_growth  # Utiliser les données de croissance par trimestre

    # Préparer les données pour le graphique
    final_df = annual_growth.reset_index().rename(columns={"close": "growth_rate"})

    # Création du graphique linéaire
    fig = go.Figure()

    # Ajouter une trace pour chaque produit sélectionné
    for commodity in selected_commodities:
        commodity_data = final_df[final_df["commodity"] == commodity]
        fig.add_trace(
            go.Scatter(
                x=commodity_data["year"] if frequency == "Année" else commodity_data["quarter"].astype(str),
                y=commodity_data["growth_rate"],  # Utiliser le taux de croissance
                mode='lines',  # Mode "lines" pour un graphique linéaire
                name=commodity
            )
        )

    # Configuration du graphique
    fig.update_layout(
        title="Growth Rates of Commodity Prices",
        xaxis_title="Année" if frequency == "Année" else "Trimestre",  # L'axe X dépend de la fréquence choisie
        yaxis_title="Taux de Croissance (%)",
        xaxis_rangeslider_visible=False,
        paper_bgcolor='rgba(0,0,0,0)',  # Fond autour du graphique transparent
        plot_bgcolor='rgba(0,0,0,0)',  # Fond de la zone de traçage transparent
    )

    # Colonne de droite : affichage du graphique
    with col2:
        st.plotly_chart(fig)

if page == "Trading volume":
    import streamlit as st
    import pandas as pd
    import plotly.graph_objects as go

    # Titre de la deuxième page
    st.title("Trading Volume Analysis")

    # Charger les données
    df = pd.read_csv('df_complet.csv')

    # Convertir la colonne 'date' en type datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    # Créer une mise en page avec deux colonnes
    col1, col2 = st.columns([2, 5])  # Largeur relative : 2 pour les widgets, 5 pour le graphique

    # Colonne de gauche : filtres
    with col1:
        # Filtre par catégorie
        categories = df["category"].unique()
        selected_category = st.selectbox(
            "Choisissez une catégorie :", categories
        )

        # Filtre par produit (basé sur la catégorie sélectionnée)
        filtered_by_category = df[df["category"] == selected_category]
        commodities = filtered_by_category["commodity"].unique()
        selected_commodities = st.multiselect(
            "Choisissez les produits à afficher :",
            commodities,
            default=commodities
        )

        # Sélection des dates (séparé en deux champs)
        min_date = df["date"].min()
        max_date = df["date"].max()

        # frequence
        frequency = st.radio(
            "Choisissez la fréquence :",
            options=["Année", "Trimestre", "Mois"]
        )

        # strart and end date
        if frequency == "Année":
            start_date = st.date_input(
                "Choisissez la date de début :",
                value=pd.to_datetime("2002-01-01"),
                min_value=pd.to_datetime("2002-01-01"),
                max_value=max_date
            )
            end_date = st.date_input(
                "Choisissez la date de fin :",
                value=pd.to_datetime("2023-12-31"),
                min_value=start_date,
                max_value=pd.to_datetime("2023-12-31")
            )

        elif frequency == "Trimestre" or frequency == "Mois":
            start_date = st.date_input(
                "Choisissez la date de début :",
                value=pd.to_datetime("2001-10-01"),
                min_value=pd.to_datetime("2001-10-01"),
                max_value=max_date
            )
            end_date = st.date_input(
                "Choisissez la date de fin :",
                value=max_date,
                min_value=start_date,
                max_value=max_date
            )

    # Filtrer les données en fonction des choix
    filtered_df = filtered_by_category[filtered_by_category["commodity"].isin(selected_commodities)]
    filtered_df = filtered_df[
        (filtered_df["date"] >= pd.Timestamp(start_date)) & (filtered_df["date"] <= pd.Timestamp(end_date))]

    # Agréger les volumes en fonction de la fréquence choisie
    if frequency == "Année":
        filtered_df["period"] = filtered_df["date"].dt.to_period("Y")
    elif frequency == "Trimestre":
        filtered_df["period"] = filtered_df["date"].dt.to_period("Q")
    elif frequency == "Mois":
        filtered_df["period"] = filtered_df["date"].dt.to_period("M")

    volume_data = filtered_df.groupby(["commodity", "period"])["volume"].sum().reset_index()

    # Création du graphique de volumes
    fig = go.Figure()

    # Ajouter une trace par produit sélectionné
    for commodity in selected_commodities:
        commodity_data = volume_data[volume_data["commodity"] == commodity]
        fig.add_trace(
            go.Bar(
                x=commodity_data["period"].astype(str),
                y=commodity_data["volume"],  # Utiliser le volume total
                name=commodity
            )
        )

    # Configuration du graphique
    fig.update_layout(
        title="Trading Volume Analysis",
        xaxis_title="Period",
        yaxis_title="Volume",
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',  # Fond autour du graphique transparent
        plot_bgcolor='rgba(0,0,0,0)',  # Fond de la zone de traçage transparent
    )

    # Colonne de droite : affichage du graphique
    with col2:
        st.plotly_chart(fig)

if page == "Volatilité des prix":
    import streamlit as st
    import pandas as pd
    import plotly.express as px


    # Fonction pour charger les données
    def load_data():
        df = pd.read_csv('df_complet.csv')
        df['date'] = pd.to_datetime(df['date'])  # Conversion de la colonne 'date' en format datetime
        return df


    # Fonction pour calculer la volatilité
    def calculate_volatility(df, period):
        df['returns'] = df['close'].pct_change()  # Calcul des variations journalières des prix
        volatility = df.groupby([pd.Grouper(key='date', freq=period), 'commodity'])[
                         'returns'].std() * 100  # Écart-type des variations
        volatility = volatility.reset_index().rename(columns={'returns': 'volatility'})
        return volatility


    # Chargement des données
    df_complet = load_data()

    # Titre de l'application
    st.title("Analyse de la volatilité des prix des matières premières")

    # Mise en page avec deux colonnes
    col1, col2 = st.columns([1, 3])  # Largeur relative : 1 pour les filtres, 3 pour le graphique

    with col1:
        # Sélection de la catégorie
        categories = df_complet['category'].unique()
        selected_category = st.selectbox("Choisissez une catégorie:", categories)

        # Filtrage par catégorie
        filtered_df = df_complet[df_complet['category'] == selected_category]

        # Sélection d'un produit (seulement un produit possible)
        commodities = filtered_df['commodity'].unique()
        selected_commodity = st.selectbox("Choisissez un produit:", commodities)

        # Filtrage par produit
        filtered_df = filtered_df[filtered_df['commodity'] == selected_commodity]

        # Sélection de la période d'agrégation
        period_map = {
            'Mois': 'ME',
            'Trimestre': 'QE',
            'Année': 'YE'
        }
        selected_period = st.selectbox("Choisissez une période d'agrégation:", list(period_map.keys()))

        # Sélection de la plage de dates
        if selected_period in ['Année', 'Mois', 'Trimestre']:
            start_date = st.date_input("Date de début:", pd.Timestamp("2001-10-01"))
        else:
            start_date = st.date_input("Date de début:", filtered_df['date'].min())

        if selected_period == 'Année':
            end_date = st.date_input("Date de fin:", pd.Timestamp("2023-12-31"))
        else:
            end_date = st.date_input("Date de fin:", filtered_df['date'].max())

    with col2:
        if start_date > end_date:
            st.error("La date de début ne peut pas être postérieure à la date de fin.")
        else:
            # Filtrage par dates
            filtered_df = filtered_df[
                (filtered_df['date'] >= pd.Timestamp(start_date)) & (filtered_df['date'] <= pd.Timestamp(end_date))]

            if filtered_df.empty:
                st.warning("Aucune donnée disponible pour les conditions sélectionnées.")
            else:
                # Calcul de la volatilité
                period = period_map[selected_period]
                volatility_df = calculate_volatility(filtered_df, period)

                # Construction du graphique
                fig = px.bar(
                    volatility_df,
                    x='date',
                    y='volatility',
                    color_discrete_sequence=['#636EFA'],  # Couleur unique pour un produit
                    title=f"Volatilité des prix pour {selected_commodity}",
                    labels={"volatility": "Volatilité (%)", "date": "Date"},
                )
                fig.update_layout(
                    bargap=0.2,
                    xaxis_title="Date",
                    yaxis_title="Volatilité (%)",
                    paper_bgcolor='rgba(0,0,0,0)',  # Fond autour du graphique transparent
                    plot_bgcolor='rgba(0,0,0,0)',  # Fond de la zone de traçage transparent
                )

                # Affichage du graphique
                st.plotly_chart(fig)

if page == "Сorrélations des prix de matières premières":
    import streamlit as st
    import pandas as pd
    import plotly.express as px


    # Fonction pour charger les données
    def load_data():
        return pd.read_csv('df_complet.csv')


    # Charger les données
    data = load_data()

    # Titre de l'application
    st.title("Carte thermique interactive des corrélations des prix de matières premières")

    # Ajouter une option "All" pour les catégories
    categories = ['All'] + list(data['category'].unique())
    selected_category = st.selectbox(
        "Sélectionnez une catégorie (ou 'All' pour toutes) :",
        options=categories
    )

    # Filtrer les commodités par catégorie sélectionnée (ou toutes si "All")
    if selected_category == 'All':
        commodities_in_category = data['commodity'].unique()
    else:
        commodities_in_category = data[data['category'] == selected_category]['commodity'].unique()

    # Ajouter une option "All" pour les commodités
    commodities = ['All'] + list(commodities_in_category)
    selected_commodities = st.multiselect(
        "Sélectionnez les produits (ou 'All' pour tous) :",
        options=commodities,
        default=['All']  # Par défaut, "All" est sélectionné
    )

    # Si l'utilisateur a sélectionné des commodités
    if selected_commodities:
        # Si "All" est sélectionné, inclure toutes les commodités dans la catégorie
        if 'All' in selected_commodities:
            filtered_data = data[data['commodity'].isin(commodities_in_category)]
        else:
            filtered_data = data[data['commodity'].isin(selected_commodities)]

        # Créer une table pivot :
        # - les lignes : commodités
        # - les colonnes : dates
        # - les valeurs : prix de clôture
        pivot_table = filtered_data.pivot_table(index='commodity', columns='date', values='close')

        # Transposer la table pivot pour obtenir commodités comme colonnes
        pivot_table_t = pivot_table.T

        # Calculer la matrice de corrélation
        corr_matrix = pivot_table_t.corr()

        # Créer une carte thermique interactive avec Plotly
        fig = px.imshow(
            corr_matrix,
            labels={'x': 'Commodity', 'y': 'Commodity', 'color': 'Correlation'},  # Étiquettes des axes
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            color_continuous_scale='Viridis'  # Échelle des couleurs
        )

        # Ajouter des annotations interactives pour afficher les corrélations au survol
        fig.update_traces(
            hovertemplate='<b>%{x} - %{y}</b><br>Correlation: %{z:.2f}<extra></extra>',  # Texte au survol
            showscale=True  # Afficher la barre de couleurs
        )

        # Mise à jour de la mise en page du graphique
        fig.update_layout(
            title='Carte Thermique des Corrélations des Matières premières',  # Titre du graphique
            xaxis_title='Commodity',  # Titre de l'axe X
            yaxis_title='Commodity',  # Titre de l'axe Y
            autosize=True,  # Ajustement automatique de la taille
            width=1000,  # Largeur du graphique
            height=800  # Hauteur du graphique
        )

        # Afficher le graphique dans Streamlit
        st.plotly_chart(fig)
    else:
        st.info("Veuillez sélectionner au moins un produit pour afficher la carte thermique.")









