
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'


def flipkart():
    driver = webdriver.Chrome()
    driver.get(url=base_url)

    all_divs = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]')
    products_divs = all_divs.find_elements(By.CLASS_NAME, '_1AtVbE col-12-12')


    for i in products_divs:
        print()
        print(i.text)


flipkart()



