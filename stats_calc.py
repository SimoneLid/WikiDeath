START_YEAR=1990
END_YEAR=2023

#calcola il numero di morti totali
def total_deaths(datas, table):
    count=0
    for year in datas.values():
        for month in year.values():
            for day in month.values():
                count+=len(day)
    table.add_row([f'Total people died', f'January {START_YEAR} - December {END_YEAR}', f'{count}'])

#calcola il numero di morti medie per anno, mese, giorno
def avg_death_year_month_day(datas, table):
    total_deaths=0
    count_year=0
    count_month=0
    count_day=0
    for year in datas.values():
        count_year+=1
        for month in year.values():
            count_month+=1
            for day in month.values():
                count_day+=1
                total_deaths+=len(day)
    table.add_row([f'Average deaths per year', f'{START_YEAR} - {END_YEAR}', "{:.2f}".format(total_deaths/count_year)])
    table.add_row([f'Average deaths per month', f'January {START_YEAR} - December {END_YEAR}', "{:.2f}".format(total_deaths/count_month)])
    table.add_row([f'Average deaths per day', f'1 January {START_YEAR} - 31 December {END_YEAR}', "{:.2f}".format(total_deaths/count_day)])

#calcola anno, mese e giorno con più morti
def year_month_most_death(datas, table):
    max_death_year=0
    year_max=[]
    max_death_month=0
    month_max=[]
    max_death_day=0
    day_max=[]
    for year, months in datas.items():
        year_death=0
        for month, days in months.items():
            month_death=0
            for day, people in days.items():
                year_death+=len(people)
                month_death+=len(people)
                if len(people)>max_death_day:
                    max_death_day=len(people)
                    day_max=[day+" "+month+" "+year]
                elif len(people)==max_death_day:
                    day_max.append([day+" "+month+" "+year])
            if month_death>max_death_month:
                max_death_month=month_death
                month_max=[month+" "+year]
            elif month_death==max_death_month:
                month_max.append(month+" "+year)
        if year_death>max_death_year:
            max_death_year=year_death
            year_max=[year]
        elif year_death==max_death_year:
            year_max.append(year)
    table.add_row(["Year with most deaths",", ".join(year_max),max_death_year])
    table.add_row(["Month with most deaths",", ".join(month_max),max_death_month])
    table.add_row(["Day with most deaths",", ".join(day_max),max_death_day])

#calcola anno e mese con meno morti
def year_month_least_death(datas, table):
    min_death_year=-1
    year_min=[]
    min_death_month=-1
    month_min=[]
    for year, months in datas.items():
        year_death=0
        for month, days in months.items():
            month_death=0
            for deaths in days.values():
                year_death+=len(deaths)
                month_death+=len(deaths)
            if month_death<min_death_month or min_death_month==-1:
                min_death_month=month_death
                month_min=[month+" "+year]
            elif month_death==min_death_month:
                month_min.append(month+" "+year)
        if year_death<min_death_year or min_death_year==-1:
            min_death_year=year_death
            year_min=[year]
        elif year_death==min_death_year:
            year_min.append(year)
    table.add_row(["Year with least deaths",", ".join(year_min),min_death_year])
    table.add_row(["Month with least deaths",", ".join(month_min),min_death_month])

#calcola età media dei morti
def avg_age_calc(datas, table):
    sum_age=0
    n_death=0
    for year in datas.values():
        for month in year.values():
            for day in month.values():
                for person in day:
                    if person["age"]!="Undefined":
                        sum_age+=person["age"]
                        n_death+=1
    table.add_row(["Average age of deaths",f'January {START_YEAR} - December {END_YEAR}',"{:.2f}".format(sum_age/n_death)])

#calcola la persona più vecchia morta
def max_age_death(datas, table):
    max_age=0
    max_age_people=[]
    day_death=[]
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                for person in people:
                    if person["age"]!="Undefined" and person["age"]>max_age and "Tree" not in person["name"]:
                        max_age=person["age"]
                        max_age_people=[person["name"]]
                        day_death=[f'{day} {month} {year}']
                    elif person["age"]==max_age:
                        max_age_people.append(person["name"])
                        day_death.append('{day} {month} {year}')
    table.add_row([f'Max age of deaths ({max_age})',", ".join(day_death),", ".join(max_age_people)])

#calcola l'età più comune
def most_common_age(datas, table):
    ages={}
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                for person in people:
                    if person["age"] in ages:
                        ages[person["age"]]+=1
                    else:
                        ages[person["age"]]=1
    common_age=max(zip(ages.values(), ages.keys()))[1]
    n_common_age=ages[common_age]
    table.add_row([f'Most common age to die ({n_common_age})', f'January {START_YEAR} - December {END_YEAR}', f'{common_age}'])

#calcola la nazionalità più comune
def most_common_nationality(datas, table):
    nationalities={}
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                for person in people:
                    if person["nation"] in nationalities:
                        nationalities[person["nation"]]+=1
                    else:
                        nationalities[person["nation"]]=1
    common_nation=max(zip(nationalities.values(), nationalities.keys()))[1]
    n_common_nation=nationalities[common_nation]
    table.add_row([f'Most common nation ({n_common_nation})', f'January {START_YEAR} - December {END_YEAR}', f'{common_nation}'])

#calcola il nome più comune
def most_common_name(datas, table):
    names={}
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                for person in people:
                    if person["name"].split()[0] in names:
                        names[person["name"].split()[0]]+=1
                    else:
                        names[person["name"].split()[0]]=1
    common_name=max(zip(names.values(), names.keys()))[1]
    n_common_name=names[common_name]
    table.add_row([f'Most common name ({n_common_name})', f'January {START_YEAR} - December {END_YEAR}', f'{common_name}'])

#calcola il nome più lungo
def longest_name(datas, table):
    long_name=0
    long_name_people=[]
    day_death=[]
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                for person in people:
                    if len(person["name"])>long_name:
                        long_name=len(person["name"])
                        long_name_people=[person["name"]]
                        day_death=[f'{day} {month} {year}']
                    elif len(person["name"])==long_name:
                        long_name_people.append(person["name"])
                        day_death.append(f'{day} {month} {year}')
    if len(day_death)>1:
        table.add_row([f'Longest name ({long_name})', f'{day_death[0]} - {day_death[-1]}',", ".join(long_name_people)])
    else:
        table.add_row([f'Longest name ({long_name})', ", ".join(day_death),", ".join(long_name_people)])

#calcola il nome più corto
def shortest_name(datas, table):
    short_name=-1
    short_name_people=[]
    day_death=[]
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                for person in people:
                    if len(person["name"])<short_name or short_name==-1:
                        short_name=len(person["name"])
                        short_name_people=[person["name"]]
                        day_death=[f'{day} {month} {year}']
                    elif len(person["name"])==short_name:
                        short_name_people.append(person["name"])
                        day_death.append(f'{day} {month} {year}')
    if len(day_death)>1:
        table.add_row([f'Shortest name ({short_name})', f'{day_death[0]} - {day_death[-1]}',", ".join(short_name_people)])
    else:
        table.add_row([f'Shortest name ({short_name})', ", ".join(day_death),", ".join(short_name_people)])

#calcola il numero di persone con una determinata nazionalità
def n_people_nationality(datas, table, nation):
    number=0
    for year in datas.values():
        for month in year.values():
            for day in month.values():
                for person in day:
                    if nation in person["nation"]:
                        number+=1
    table.add_row([f'People with {nation} nationality', f'January {START_YEAR} - December {END_YEAR}', f'{number}'])

#calcola il numero di persone con una determinata età
def n_people_age(datas, table, age):
    number=0
    for year in datas.values():
        for month in year.values():
            for day in month.values():
                for person in day:
                    if age==person["age"]:
                        number+=1
    table.add_row([f'People died at {age}', f'January {START_YEAR} - December {END_YEAR}', f'{number}'])

#trova il numero di persone con un determinato nome
def search_name(datas, table, name):
    count=0
    day_death=[]
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                for person in people:
                    if name in person["name"]:
                        count+=1
                        day_death.append(f'{day} {month} {year}')
    if len(day_death)>1:
        table.add_row([f'People with name {name}', f'{day_death[0]} - {day_death[-1]}', count])
    elif len(day_death)==1:
        table.add_row([f'People with name {name}', ", ".join(day_death),count])

#trova il numero di persone morte in un determinato giorno
#(giorno obbligatorio, mese e anno opzionali)
def search_date(datas, table, date):
    count=0
    day_death=[]
    for year, months in datas.items():
        for month, days in months.items():
            for day, people in days.items():
                if date in day+" "+month+" "+year and date.split(" ")[0]==day:
                    count+=len(people)
                    day_death.append(f'{day} {month} {year}')
    if len(set(day_death))>1:
        table.add_row([f'People died in {date}', f'{day_death[0]} - {day_death[-1]}', count])
    elif len(set(day_death))==1:
        table.add_row([f'People died in {date}', day_death[0], count])