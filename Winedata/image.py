from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



wine_name = ["레드와인","화이트와인", "체다치즈", "다람쥐"]
url = "https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl"
driver = webdriver.Chrome('chromedriver.exe')
options = webdriver.ChromeOptions()
driver.get(url)

for i in wine_name:
   elem = driver.find_element(By.NAME, "q")
   elem.clear()
   elem.send_keys(i)
   elem.send_keys(Keys.RETURN)

   # driver.find_element(By.CLASS_NAME,".Q4LuWd").click()

   html = driver.page_source
   soup = BS(html,features="html.parser")

   div_img = soup.select_one('.OUZ5W')
   img = div_img.select_one('img')['src']

   print(img)



