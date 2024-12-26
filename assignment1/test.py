import pandas as pd
from bs4 import BeautifulSoup
import requests
# to get data from website
file = requests.get(
    "https://weather.com/en-CA/weather/tenday/l/774e43da3c5f218cdf671f93ca3cb901c5ff0731691a2577929bb2ecc3d4e5c1")

# import Beautifulsoup for scraping the data
soup = BeautifulSoup(file.content, "html.parser")
# print(soup.prettify())
# create empty list
list = []
all = soup.find(
    # "div", {"class": "locations-title ten-day-page-title"}).find("h1").text
    "div", {"class": "LocationPageTitle--LocationPageTitle--UGFbm DailyForecast--CardHeader--bTsLT"}).find("h1").text
print(all)
# <div class="LocationPageTitle--LocationPageTitle--UGFbm DailyForecast--CardHeader--bTsLT"><h1 class="LocationPageTitle--PageHeader--amwRZ"><strong>10 Day Weather</strong><span class="LocationPageTitle--LocationText--l3ftJ">-<span data-testid="PresentationName" class="LocationPageTitle--PresentationName--YxTV7">Toronto, Ontario</span></span></h1></div>

# find all table with class-"twc-table"
content = soup.find_all("table", {"class": "twc-table"})
for items in content:
    for i in range(len(items.find_all("tr"))-1):
        # create empty dictionary
        dict = {}
        try:
            # assign value to given key

            dict["day"] = items.find_all(
                "span", {"class": "date-time"})[i].text
            dict["date"] = items.find_all(
                "span", {"class": "day-detail"})[i].text
            dict["desc"] = items.find_all(
                "td", {"class": "description"})[i].text
            dict["temp"] = items.find_all("td", {"class": "temp"})[i].text
            dict["precip"] = items.find_all("td", {"class": "precip"})[i].text
            dict["wind"] = items.find_all("td", {"class": "wind"})[i].text
            dict["humidity"] = items.find_all(
                "td", {"class": "humidity"})[i].text
        except:
            # assign None values if no items are there with specified class

            dict["day"] = "None"
            dict["date"] = "None"
            dict["desc"] = "None"
            dict["temp"] = "None"
            dict["precip"] = "None"
            dict["wind"] = "None"
            dict["humidity"] = "None"

        # append dictionary values to the list
        list.append(dict)

convert = pd.DataFrame(list)
convert.to_csv("output.csv")

# read csv file using pandas
a = pd.read_csv("output.csv")
print(a)
