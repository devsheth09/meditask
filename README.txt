The main.py file contains all the code required. The data folder contains the data used for this project.

The following packages need to be installed for this to work:
- json
- fastapi

The root url
http://127.0.0.1:8000/
shows the full data

To sort the entire list by item's price,
http://127.0.0.1:8000/getsorteddata?reverse=True&criteria=price

To get any item by id
http://127.0.0.1:8000/getitem?id=54092a8659896c3313000098

To get any item by location
http://127.0.0.1:8000/getitem?location=[31.212990610939393,121.5804870980477]

To get list of items by status
http://127.0.0.1:8000/getitemslist?status=removed

To get list of items by User Id
http://127.0.0.1:8000/getitemslist?userid=53f6c9c96d1944af0b00000b

To get list of items based on radius and location
http://127.0.0.1:8000/get_items_in_radius?radius=10&latitude=36&longitude=115