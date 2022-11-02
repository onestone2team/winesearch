from urllib.request import urlretrieve
from urllib.parse import quote_plus    
from bs4 import BeautifulSoup as BS    
from selenium import webdriver

wine_name = input("wine : ")
wine_name = wine_name.replace('','+')
i_url = f'https://www.google.com/search?q={wine_name}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi4rtfAq4_7AhXRq1YBHaI3B7oQ_AUoAnoECAEQBA&biw=967&bih=554&dpr=1.25#imgrc=aWODM-gjNv81jM'
driver = webdriver.Chrome('C://chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get(i_url)

html = driver.page_source
soup = BS(html,features="html.parser")

img = soup.select('img')

image_list = []
count = 1

print("Searching...")
for i in img:
   try:
      image_list.append(i.attrs["src"])
   except KeyError:
      image_list.append(i.attrs["data-src"])

print("Downloading...")
for i in image_list:
   urlretrieve(i,"download/"+wine_name+str(count)+".jpg")
   count+=1

driver.close()
print("집에가자")
