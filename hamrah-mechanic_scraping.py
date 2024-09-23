from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector
options = Options()
driver = webdriver.Chrome(options=options)
url = 'https://www.hamrah-mechanic.com/cars-for-sale/'
driver.get(url)
SCROLL_PAUSE_TIME = 60
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
html_content = driver.page_source
driver.quit()  
soup = BeautifulSoup(html_content, "html.parser")
car_info = soup.find_all("div", class_="card_general-card__pj_NR carCard_card__XyDuv list_card__WCLwO")

pattern_car_name = r'(.+?)\s+مدل'
pattern_age = r'مدل\s+(\d{4})'
car_list = []

for tag in car_info:
    car_name_tag = tag.find("span", class_="carCard_header__name__ib5RB")
    car_function_tag = tag.find("span", class_="carCard_specification__item-text__2c1Ub", dir="ltr")
    car_price_tag = tag.find("div", class_="carCard_price-container__cost__BO_Hy")
    
    if car_name_tag and car_function_tag and car_price_tag:
        car_name_info = car_name_tag.get_text(strip=True)
        car_name_match = re.search(pattern_car_name, car_name_info)
        production_year_match = re.search(pattern_age, car_name_info)
        
        if car_name_match and production_year_match:
            car_name = car_name_match.group(1)
            production_year = production_year_match.group(1)
            car_function = car_function_tag.get_text(strip=True)
            car_price = car_price_tag.get_text(strip=True)
        
            car_list.append((car_name, production_year, car_function, car_price))
cnx = mysql.connector.connect(
    user='kian',
    password='Kian.py192',
    host='127.0.0.1',
    database='fina_project',
    auth_plugin='mysql_native_password'
)#If you want to use this code, enter your database information in this line
cursor=cnx.cursor()
query="INSERT INTO info (car_name,production_year,car_function,car_price) VALUES (%s,%s,%s,%s);"

for item in car_list:
    
    cleaned_text = [re.sub(r'\s*تومان\s*|\s*KM\s*$', '', text) for text in item]
    name=cleaned_text[0]
    year=cleaned_text[1]
    function=cleaned_text[2]
    price=cleaned_text[3]
    if function == "صفر":
        function = function.replace('صفر', '0')

    cursor.execute(query,(name,year,function,price))
cnx.commit()
cursor.close()
cnx.close()

