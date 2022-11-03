from urllib.request import urlretrieve 
from bs4 import BeautifulSoup as BS    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



wine_name = ["레드와인","화이트와인", "체다치즈", "다람쥐"]
# wine_name = wine_name.replace(' ','+')
# i_url = f'https://www.google.com/search?q={wine_name}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi4rtfAq4_7AhXRq1YBHaI3B7oQ_AUoAnoECAEQBA&biw=967&bih=554&dpr=1.25#imgrc=aWODM-gjNv81jM'

url = "https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl"
driver = webdriver.Chrome('chromedriver.exe')

options = webdriver.ChromeOptions()

driver.get(url)

for i in wine_name:
   elem = driver.find_element(By.NAME, "q")
   elem.clear()
   elem.send_keys(i)
   elem.send_keys(Keys.RETURN)

   driver.find_element(By.XPATH,"//*[@id='islrg']/div[1]/div[1]").click()

   html = driver.page_source
   soup = BS(html,features="html.parser")

   div_img = soup.select_one('.pxAole')
   img = div_img.select_one('img')['src']
   
   print(img)
   

