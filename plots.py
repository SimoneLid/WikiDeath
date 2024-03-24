import matplotlib.pyplot as plt
from datetime import datetime


START_YEAR=1990
END_YEAR=2023

#crea un grafico con il numero di morti al mese
def plot_month_deaths(datas):
    month_deaths={}
    for year, months in datas.items():
        for month, days in months.items():
            month_death_count=0
            for day, people in days.items():
                month_death_count+=len(people)
            month_deaths[month+" "+year]=month_death_count
    month_date=[datetime(y,m,1) for y in range(START_YEAR,END_YEAR+1) for m in range(1,13)]
    plt.plot(month_date, month_deaths.values())
    plt.suptitle("Deaths per month")
    plt.xticks(rotation=45)
    plt.show()