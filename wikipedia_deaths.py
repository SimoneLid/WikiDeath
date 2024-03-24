import create_DB_death
import stats_calc
import plots
import json
from prettytable import PrettyTable


START_YEAR=1990
END_YEAR=2023
FORCE_DB=False


#apre il json, carica i dati e crea la tabella
def data_from_json(filename):
    with open(filename, "r") as json_file:
        datas=json.load(json_file)
    return datas


#statistiche generali
def general_statistics(filename):
    datas= data_from_json(filename)
    table=PrettyTable()
    table.field_names=["Stat","Period of Time","Number/Name"]
    stats_calc.total_deaths(datas, table)
    stats_calc.avg_death_year_month_day(datas, table)
    stats_calc.year_month_most_death(datas, table)
    stats_calc.year_month_least_death(datas, table)
    stats_calc.avg_age_calc(datas, table)
    stats_calc.max_age_death(datas, table)
    stats_calc.most_common_age(datas, table)
    stats_calc.most_common_nationality(datas, table)
    stats_calc.most_common_name(datas , table)
    #stats_calc.longest_name(datas, table)
    stats_calc.shortest_name(datas, table)
    print("----------------------------------------- General Stats ----------------------------------------")
    print(table)


#statistiche specificate da utente
def specified_statistics(filename):
    datas= data_from_json(filename)
    table=PrettyTable()
    table.field_names=["Stat","Period of Time","Number/Name"]
    stats_calc.n_people_nationality(datas, table, "Italian")
    stats_calc.n_people_age(datas, table, 69)
    stats_calc.search_name(datas, table, "Queen Elizabeth II")
    stats_calc.search_date(datas, table, "25")
    print("---------------------------------------- Specific Stats ----------------------------------------")
    print(table)

def plot(filename):
    datas=data_from_json(filename)
    plots.plot_month_deaths(datas)

if __name__=="__main__":
    create_DB_death.create_database_death(START_YEAR, END_YEAR, FORCE_DB)
    general_statistics("death_database.json")
    specified_statistics("death_database.json")
    plot("death_database.json")
