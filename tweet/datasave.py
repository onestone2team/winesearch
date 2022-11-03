# import json

# file_path = "tweet\sample.json"
# list = []
# with open(file_path, "r") as json_file:
#     json_data = json.load(json_file)
#     for i in range(len(json_data)):
#         name = json_data[i]["title"]
#         content = json_data[i]["description"]
#         tag = json_data[i]["variety"]
#         country = json_data[i]["country"]

#         list.append({"name":name, "content":content, "tag":tag, "country":country})

# pprint.pprint(list)


import json
import pprint

f = open('tweet\sample.json')
  
json_data = json.load(f)
list = []
for i in range(len(json_data)):
        name = json_data[i]["title"]
        content = json_data[i]["description"]
        tag = json_data[i]["variety"]
        country = json_data[i]["country"]

        list.append({"name":name, "content":content, "tag":tag, "country":country})

pprint.pp(list)

f.close()




'''
from urllib.request import urlretrieve 
from bs4 import BeautifulSoup as BS    
from selenium import webdriver
import json
import pprint


file_path = "tweet\sample.json"
list = []
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)
    for i in range(len(json_data)):
        name = json_data[i]["title"]
        content = json_data[i]["description"]
        tag = json_data[i]["variety"]
        country = json_data[i]["country"]

        wine_name = name
        wine_name = wine_name.replace(' ','+')
        i_url = f'https://www.google.com/search?q={wine_name}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi4rtfAq4_7AhXRq1YBHaI3B7oQ_AUoAnoECAEQBA&biw=967&bih=554&dpr=1.25#imgrc=aWODM-gjNv81jM'
        driver = webdriver.Chrome('chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver.get(i_url)
        html = driver.page_source
        soup = BS(html,features="html.parser")

        div_img = soup.select_one('.bRMDJf')
        img = div_img.select_one('img')['src']


        list.append({"name":name, "content":content, "tag":tag, "country":country, "image":img})
        pprint.pp(list)



'''

