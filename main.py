import json
from fastapi import FastAPI
app = FastAPI()

f = open('data/craiglist')
data_dict = json.load(f)

def dist(a, b, lat, long):
    return ((lat - a)**2 + (long - b)**2)**0.5

@app.get("/")
def root():
    return data_dict

@app.get("/getsorteddata")
def root(reverse : bool , criteria : str):
    try:
        result = sorted(data_dict, key=lambda x:x[criteria], reverse= reverse)
        return result
    except:
        print("Check that Criteria mentioned is a valid column and reverse is a boolean value")


@app.get("/getitem")
def root(id: str | None = None , location: str | None = None):
    try:
        if id:
            result = list(filter(lambda x : x['id'] == id, data_dict))
        else:
            result = list(filter(lambda x: x['loc'][0] == location[0] and x['loc'][1] == location[1], data_dict))
        return result
    except:
        print("Check if the Id passed is a valid value and location is passed in a list.")

@app.get("/getitemslist")
def root(status: str | None = None , userid: str | None = None):
    try:
        if status:
            result = list(filter(lambda x : x['status'] == status, data_dict))
        else:
            result = list(filter(lambda x: x['userId'] == userid, data_dict))
        return result
    except:
        print("Check the values passed in the url are valid values.")

@app.get("/get_items_in_radius")
def root(radius: int, latitude: int, longitude: int):
    try:
        result = [x for x in data_dict if dist(x['loc'][0], x['loc'][1], latitude, longitude) <= radius ]
        return result
    except:
        print("Check that the values passed are numbers.")



#http://127.0.0.1:8000/getsorteddata?reverse=True&criteria=price