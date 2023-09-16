from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time



def form_submit_driver():

   url = 'http://127.0.0.1:8000/companies/'
   chrome_options = Options()
   chrome_options.add_experimental_option('detach', True)
    
   mydriver = webdriver.Chrome(options=chrome_options)
   mydriver.get(url)
   
   # comp name
   mydriver.find_element(By.XPATH, '/html/body/div/form/div[1]/input').send_keys('MY Company name')
   
   # comp type
   mydriver.find_element(By.XPATH, '/html/body/div/form/div[2]/input').send_keys('Random Company Type')
   
   # compnay headq
   mydriver.find_element(By.XPATH, '/html/body/div/form/div[3]/input').send_keys('Mumbai')

   # how old
   mydriver.find_element(By.XPATH, '/html/body/div/form/div[4]/input').send_keys('10 yeasr')
   
   # open jobs
   mydriver.find_element(By.XPATH, '/html/body/div/form/div[5]/input').send_keys('100')

   # services
   mydriver.find_element(By.XPATH, '/html/body/div/form/div[6]/textarea').send_keys('Companies Services here')

   # descriptn
   mydriver.find_element(By.XPATH, '/html/body/div/form/div[7]/textarea').send_keys('Companie description')

   # companies no of emp

   mydriver.find_element(By.XPATH, '/html/body/div/form/div[8]/input').send_keys('10 Lacks')

   #submit btn
   mydriver.find_element(By.XPATH, '/html/body/div/form/button').click()

   time.sleep(60*1)


form_submit_driver()