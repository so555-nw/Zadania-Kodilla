# sqlalchemy_ex_02.py
# uzyje biblioteki pandy do tego zadania
import pandas as pd
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("sqlite:///data.db")

measure = pd.read_csv("clean_measure.csv")
stations = pd.read_csv("clean_stations.csv")

stations.to_sql("stations", engine, if_exists="replace", index=False)
measure.to_sql("measure", engine, if_exists="replace", index=False)

with engine.connect() as conn:
    task = conn.execute(text("SELECT id FROM stations"))


    print(" id ze stations:")
    for row in task:
        print(row)