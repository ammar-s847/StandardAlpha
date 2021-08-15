import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient

# Config
from config import MONGO_CONNECT_STR

# Mongo
mongo = MongoClient(MONGO_CONNECT_STR)
db1 = mongo.get_database('financial_data')
stock_data = db1.stock_data

# Convert Stock_data entry to a DataFrame
def stock_data_to_df(data):
    data_list = []
    for i in data["data"]:
        entry = [data["symbol"]]
        entry.append(i)
        entry.append(data["data"][i]["open"])
        entry.append(data["data"][i]["high"])
        entry.append(data["data"][i]["low"])
        entry.append(data["data"][i]["close"])
        entry.append(data["data"][i]["volume"])
        data_list.append(entry)
    
    return pd.DataFrame(data_list, columns=["symbol", "timestamp", "open", "high", "low", "close", "volume"])


# Get specific data from the database
def get_data(symbol, time_range="day", **kwargs):
    if time_range == "day" and "day" in kwargs: 
        return "1"
    elif time_range == "day" and "day" not in kwargs:
        return "2"

    #test
    if time_range == "test":
        data = stock_data.find_one({"symbol":symbol, "day":"2021-06-11"})
        return stock_data_to_df(data).tail(10)

print(get_data("TSLA", "test"))

# Data cleaning
def clean_data(data):
    return ""



# Visualization
def graph_one_day(df):
    return ""

# Prediction