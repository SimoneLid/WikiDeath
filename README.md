# WikiDeath
 
Programma che crea un database con tutte le morti celebri listate su wikipedia nelle pagine Deaths_in_Month_Year dal Gennaio 1990 fino a Dicembre 2023. Le morti vengono divise per giorno e di ogni persona viene salvato nome, età di morte e nazionalità (nel caso in cui non siano disponibili la persona viene ignorata).<br>
Una volta creato il database vengono calcolate alcune statistiche, sia generali che specifiche, sulle morti: ad esempio anno con più morti, età media di morte, ecc...<br>
Queste statistiche vengono printate in una tabella tramite il pacchetto prettytable e viene anche creato un grafico delle morti per ogni mese tramite il pacchetto matplotlib.
### Esempio di output
|Tabella|Grafico|
|:-----:|:-----:|
|<img src="table_example.png" alt="image" width="auto" height="auto">|<img src="plot_example.png" alt="image" width="auto" height="auto">|