import requests
from pymongo import MongoClient
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

# use CRON in Python (python-crontab)
# use sentiment analysis tool and prediction models to display prediction data on user tracked stocks.
app = Flask(__name__)
api = Api(app)
CORS(app)

# Globals ---------------------------------------------------------------------
from config import AV_URL, AV_KEY, MONGO_CONNECT_STR
tracking = []

# Connect to MongoDB ----------------------------------------------------------
mongo = MongoClient(MONGO_CONNECT_STR)
db = mongo.get_database('financial_data')
stock_data = db.stock_data

# Track stocks (upon boot-up) -------------------------------------------------
def bootup_tracking_list():
    global tracking
    tracking = stock_data.find_one({"global":"tracking"})["data"]
    if tracking == None or len(tracking) == 0: # empty tracking set upon boot-up
        stock_data.update_one({"global":"tracking"}, {"$set":{"global":"tracking", "data":['IBM', 'TSLA', 'AAPL']}}) # load sample stocks

bootup_tracking_list()

# Update Tracking List --------------------------------------------------------
def add_tracking_list(input=[]): # enter a list of symbols to add to the tracking set
    global tracking
    current_list = stock_data.find_one({"global":"tracking"})["data"]
    for i in input:
        if i in current_list:
            input.remove(i)
    current_list.extend(input)
    stock_data.update_one({"global":"tracking"}, {"$set":{"global":"tracking", "data":current_list}})
    tracking = current_list

# Request data from Alpha Vantage API -----------------------------------------
def request_data(symbol):
    try:
        response = requests.get(AV_URL + f"?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={AV_KEY}")
        return response.json()
    except:
        return "error"

#print(request_data("TSLA"))

# Clean Alpha Vantage data ----------------------------------------------------
def clean_data(data):
    if data != "error":
        output = {"symbol":"", "day":"", "data":{}}
        output["symbol"] = data["Meta Data"]["2. Symbol"]
        output["day"] = data["Meta Data"]["3. Last Refreshed"][:10]
        output["data"] = data["Time Series (5min)"]
        for i in output["data"]:
            output["data"][i]["open"] = output["data"][i]["1. open"]
            del output["data"][i]["1. open"]
            output["data"][i]["high"] = output["data"][i]["2. high"]
            del output["data"][i]["2. high"]
            output["data"][i]["low"] = output["data"][i]["3. low"]
            del output["data"][i]["3. low"]
            output["data"][i]["close"] = output["data"][i]["4. close"]
            del output["data"][i]["4. close"]
            output["data"][i]["volume"] = output["data"][i]["5. volume"]
            del output["data"][i]["5. volume"]
        return output
    else:
        return "error"
    
#print(clean_data(request_data("IBM")))

# Insert data into MongoDB ----------------------------------------------------
def insert_stock_data(symbol):
    stock_data.insert_one(clean_data(request_data(symbol)))

def select_stock_data(symbol, day, time=None):
    pass

# Flask RESTful API -----------------------------------------------------------
class Parameters(Resource):
    def get(self, function, f_input=None):

        # Test get request
        if function == "test":
            pass

        # Manually update tracking list variable
        elif function == "bootup-tracking-list":
            bootup_tracking_list()
            return {"status":"200", "output":"rebooted tracking list"}
            
        # Get the current Tracking List in the database
        elif function == "get-tracking-list":
            output = ""
            if tracking != None and len(tracking) > 0:
                output = " ".join(tracking)
            return {"status":"200", "output":output}

        # Add stocks to the tracking list
        elif function == "add-tracking-list":
            # f_input: stock symbols seperated by "-" symbols
            if f_input != None and len(f_input) > 0:
                add_tracking_list(f_input.split("-"))
                return {"status":"200", "output":f"added {f_input} to the tracking list. Tracking List = {' '.join(tracking)}"}
            else:
                return {"status":"400", "output":"invalid input"}



        # Invalid Input
        else:
            return {"status":"400", "output":"Invalid Input"}

class DataRequest(Resource):
    def get(self, function, f_input):
        return {"message":f"using {function}"}

api.add_resource(Parameters, "/param/<string:function>", "/param/<string:function>/<string:f_input>")
api.add_resource(DataRequest, "/req/<string:function>", "/req/<string:function>/<string:f_input>")

if __name__ == "__main__":
    app.run(debug=True)