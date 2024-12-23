# Projet C -Data analyse de données financières sur les marchés

## Les différentes méthodes de visualisation

- **Aire (Area chart)**

    - Un graphique d'aire met en évidence les variations d'une quantité dans le temps en remplissant l'espace sous une courbe. Cela aide à visualiser des tendances cumulatives ou des changements globaux.

        - Exemple d'usage : Suivi des revenus cumulés, des volumes ou des proportions.
        - Avantage : Visuellement intuitif pour des séries temporelles ou des données continues.

[Python](/Area_chart/Area_chart.py)

[R](/Area_chart/Area_chart.R)

---

- **Diagramme en barres colorées (colored bar chart)**

    - Un diagramme en barres colorées est utilisé pour comparer des catégories ou des valeurs discrètes. Les couleurs des barres peuvent indiquer des informations supplémentaires, comme des variations positives ou négatives.

        - Exemple d'usage : Comparer les performances d’équipes, visualiser des hausses/baisses de ventes.
        - Avantages : Facile à interpréter, permet de mettre en évidence des tendances ou des valeurs spécifiques.

[Python](Colored_bar_chart/Colored_bar_chart.py)

[R](Colored_bar_chart/Colored_bar_chart.R)

---

- **Bougies Japonaises (Candlestick Chart)**

    - Un graphique en bougies japonaises est utilisé pour représenter les mouvements des prix sur une période donnée. Chaque bougie montre quatre informations clés :
         
        - Ouverture (Open)
        - Clôture (Close)
        - Plus haut (High)
        - Plus bas (Low)

    - Les bougies sont souvent colorées :

        - Verte ou blanche : Clôture au-dessus de l'ouverture (hausse).
        - Rouge ou noire : Clôture en dessous de l'ouverture (baisse).

[Python](Candlestick_chart/Candlestick_chart.py)

[R](Candlestick_chart/Candlestick_chart.r)

---

- **Heikin Ashi**

    - Le graphique Heikin Ashi est une variante des bougies japonaises. Il utilise des valeurs moyennes pour lisser les variations des prix et identifier plus clairement les tendances. Contrairement aux bougies traditionnelles, chaque bougie Heikin Ashi est calculée à partir de la bougie précédente et des prix actuels.

    - Formules des bougies Heikin Ashi :
        1. Open = (Open précédent + Close précédent) / 2
        2. Close = (Open actuel + High actuel + Low actuel + Close actuel) / 4
        3. High = Le maximum de (High actuel, Open Heikin Ashi, Close Heikin Ashi)
        4. Low = Le minimum de (Low actuel, Open Heikin Ashi, Close Heikin Ashi)

    Les bougies rouges indiquent une tendance baissière, et les bougies vertes une tendance haussière.

[Python](/Heikin_Ashi/Heikin_ashi.py)

[R](/Heikin_Ashi/Heikin_ashi.r)

---

- **Hollow Candle (Bougies Creuses)**

    - Les hollow candles (ou bougies creuses) sont similaires aux bougies japonaises, mais avec une distinction visuelle supplémentaire :

        - Une bougie creuse (hollow) indique que la clôture est supérieure à l'ouverture (tendance haussière).
        - Une bougie remplie indique que la clôture est inférieure à l'ouverture (tendance baissière).
        - Les couleurs vertes et rouges peuvent être utilisées pour renforcer l’indication haussière ou baissière.

[Python](/Hollow_candle/Hollow_candle.py)

[R](/Hollow_candle/Hollow_candle.R)

---

- **Kagi**

    - Le graphique Kagi est un type de graphique utilisé principalement dans l'analyse technique pour représenter les variations de prix sans tenir compte du temps.
Il met en évidence les changements significatifs de tendance en fonction d’un seuil (appelé "reversal amount").

        - Les lignes changent d’épaisseur ou de couleur selon la direction du prix.
        - Il ne suit pas les mouvements mineurs, ce qui permet de se concentrer sur les tendances majeures.
        - Souvent utilisé pour identifier des niveaux de support et de résistance.

[python](/Kagi/Kagi.py)

 [R](/Kagi/Kagi.R)

 ---

- **Lignes**

    - Un graphique en lignes relie les points de données d'une série temporelle ou d'autres catégories avec des segments de ligne. Il est souvent utilisé pour visualiser les tendances ou suivre les changements sur une période.

        - Exemple d'usage : Analyse des prix des actions, visualisation de données météo, etc.

        - Avantages : Simple, efficace pour identifier les tendances générales.

[Python](/Lignes/Lignes.py)

[R](/Lignes/Lignes.r)

---

- **Line break**

    - Un graphique Line Break est un type de graphique sans échelle temporelle qui met en évidence les changements significatifs de prix.

        - Chaque ligne représente un mouvement de prix : une ligne verte (ou haussière) pour une hausse, une ligne rouge (ou baissière) pour une baisse.

        - Un nouveau bloc est dessiné uniquement si le prix dépasse un certain seuil par rapport aux blocs précédents.

        - Cela filtre les petits mouvements et permet de mieux observer les tendances principales.

[Python](/Line_break/Line_break.py)

[R](/Line_break/Line_break.r)

---

- **Graphique Renko**

    - Un graphique Renko est utilisé pour filtrer les fluctuations mineures de prix afin de se concentrer sur les grandes tendances. Il est composé de "briques" de taille fixe (définie par un seuil) :

        - Une nouvelle brique haussière est ajoutée lorsque le prix monte au-dessus de la clôture précédente d'au moins la taille du seuil.

        - Une brique baissière est ajoutée lorsque le prix descend en dessous de la clôture précédente d'au moins la taille du seuil.

    Les graphiques Renko ignorent le temps et se concentrent uniquement sur les mouvements de prix.

[Python](/Renko/Renko.py)

[R](/Renko/Renko.r)

## dataviz chandelles 

Ce script génère des données financières simulées, calcule l'écart-type des prix de clôture et affiche un graphique en chandelles avec l'écart-type sur les prix de clôture.

### Explications du Code - Dataviz Chandelles

1 . Importation des bibliothèques : Importation des bibliothèques nécessaires ```(pandas, numpy, matplotlib, mplfinance)```.

2 . Génération des données : Création de données financières factices avec des prix d'ouverture, de clôture, les plus hauts et bas, ainsi que les volumes.

3 . Renommage des colonnes : Mise en conformité des noms des colonnes pour ```mplfinance```.

4 . Calcul de l'écart-type : Calcul de l'écart-type des prix de clôture pour mesurer la volatilité du marché.

5 . Graphique en chandelles : Affichage d'un graphique en chandelles avec ```mplfinance```, montrant l'évolution des prix.

6 . Statistiques descriptives : Affichage des statistiques descriptives des prix de clôture (moyenne, écart-type, etc.).

7 . Visualisation de l'écart-type : Tracé des prix de clôture avec les lignes représentant la moyenne et l'écart-type.

[code](/dataviz_chandelles_volatilite.py)

## Reconstruction de la Distribution de Probabilité à partir d'une Marche Aléatoire

Ce script simule une marche aléatoire en utilisant des rendements journaliers normalement distribués, puis reconstruit et affiche la distribution de probabilité des rendements.


### Explications du Code

1 . Importation des bibliothèques : Importation des bibliothèques nécessaires ```(numpy, pandas, matplotlib, scipy)```.

2 . Génération des données :

- ```dates``` : Création de 100 jours ouvrés.

- ```returns``` : Génération de rendements journaliers suivant une distribution normale (moyenne de 0 et écart-type de 0,01).

3 . Simulation des prix : Les prix sont simulés en cumulant les rendements journaliers à partir d'un prix initial de 100.

4 . Calcul des rendements journaliers : Les rendements journaliers sont calculés en prenant la différence entre les prix consécutifs.

5 . Estimation de la distribution de probabilité :

- Un histogramme des rendements est tracé.

- Une courbe de distribution normale est ajustée aux données des rendements simulés.

6 . Affichage des résultats : Le script affiche la moyenne et l'écart-type des rendements, et montre la courbe de densité ajustée.

[code](/marche_aleatoire_distribution.py)

---

Projet réaliser par Pierre et Lukas.

