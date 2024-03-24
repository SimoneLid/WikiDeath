import wikipediaapi
import json
import os
from prettytable import PrettyTable


WIKI=wikipediaapi.Wikipedia('MyProjectName','en')
MONTHS=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def create_URLs(start_year, end_year):
    URLs=[]
    for year in range(start_year, end_year+1):
        for month in MONTHS:
            URLs.append("Deaths_in_"+month+"_"+str(year))
    return URLs

def control_URLs_existance(URLs):
    sum=0
    not_exist=[]
    for URL in URLs:
        if WIKI.page(URL).exists():
            sum+=1
        else:
            not_exist.append(URL)
    print("Esistono",sum,"pagine su",len(URLs))
    if len(not_exist)>0:
        print("Non esistono:",not_exist)

def page_text(URL):
    print("Dumping:",URL)
    page=WIKI.page(URL)
    return page.text

def create_dict_month(page):
    text=page_text(page)
    text=text.replace(":","\n")
    lines=text.split("\n")
    lines=cut_start_end(lines)
    days_lines=divide_word_day(lines)
    month_death_classified={}
    for day, lines in days_lines.items():
        for line in lines[1:]:
            try:
                datas=line.split(",")
                name=datas[0].strip()
                age=int(datas[1].split("–")[0].split("-")[0].strip())
            except:
                continue
            if age<1 or age>123 or len(name)<1 or len(name)>50:
                continue
            if len(datas)>2:
                nationality=datas[2].split()[0].strip()
            else:
                nationality="Undefined"
            if day in month_death_classified.keys():
                month_death_classified[day].append({"name":name,"age":age,"nation":nationality})
            else:
                month_death_classified[day]=[{"name":name,"age":age,"nation":nationality}]
    return month_death_classified

def cut_start_end(lines):
    start=0
    for i in range(len(lines)):
        if lines[i]=='1':
            start=i
        elif lines[i]=="" and lines[i+1]=="" and start!=0:
            end=i
            break
    return lines[start:end]

def divide_word_day(lines):
    count=1
    days_lines={}
    day_words=[]
    for i in range(len(lines)):
        if lines[i]=="" and lines[i+1]==str(count+1):
            days_lines[str(count)]=day_words
            day_words=[]
            count+=1
        else:
            day_words.append(lines[i])
    days_lines[str(count)]=day_words
    return days_lines

def create_database_death(start_year, end_year, FORCE_DB=False):
    if FORCE_DB or os.path.exists("death_database.json")==False:
        table=PrettyTable()
        table.field_names=["Month","Number of Deaths"]
        pages=create_URLs(start_year, end_year)
        #control_URLs_existance(pages)
        death_list={}
        for year in range(start_year, end_year+1):
            death_list[str(year)]={}
        for month_page in pages:
            year=month_page.split("_")[3]
            month=month_page.split("_")[2]
            month_death_classified=create_dict_month(month_page)
            death_list[year][month]=month_death_classified
            table.add_row([month+" "+year, sum(len(v) for v in month_death_classified.values())])
        with open("death_database.json", "w") as db:
            json.dump(death_list,db,indent=4)
        print("-------------------------------------- Database Completed --------------------------------------")
        print(table)
    else:
        print("------------------------------------ Database already exist ------------------------------------")