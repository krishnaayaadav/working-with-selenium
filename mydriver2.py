from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

def get_page():
   url = 'http://scrappers.pythonanywhere.com/flipkart-products/scrapper/?page=2'

   driver = webdriver.Chrome()
   driver.get(url)

   for i in range(3):

      try:
         elm = driver.find_element(By.XPATH, '/html/body/div/div[2]/nav[1]/ul/li[5]/a/span').click()
      except:
         print('No elm found')
      else:
         print('Yes elm found')
         pass


# get_page()


def youtube_data_extractor():
   url  = 'https://www.youtube.com/@JohnWatsonRooney'
   
   driver = webdriver.Chrome()
   driver.get(url)
   driver.implicitly_wait(11)

   try:
      all_div = driver.find_element(By.ID, 'items')
   except:
      print('No Items found')
   else:

      for items in all_div:
         try:
            title = items.find_element(By.ID, "video-title")
         except:
            print('Title not found')
         else:
            print(title.text)


         try:
            views = items.find_element(By.CLASS_NAME, 'style-scope ytd-grid-video-renderer')
         except:
            print('Video Views not found')

            pass
         else:
            print(views.text)

         try:
            times  = items.find_elements(By.CLASS_NAME,'style-scope ytd-grid-video-renderer')
         except:
            print('Times Published not found')
         else:
            print(times.text)

         
# youtube_data_extractor()

def news_app_scrappers():
   url = 'http://127.0.0.1:8000/myapp/homepage/'
   paths = 'C:/Users/HP/Desktop/AllCredentials/chromedriver'

   # Connect
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_experimental_option("detach", True)
   chrome_options.add_argument("--incognito")
   global driver # this will prevent the browser variable from being garbage collected
   driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
   driver.set_window_size(900, 900)
   driver.get(url)
   global all_trs, tbody
   tbody = driver.find_element(By.TAG_NAME, 'tbody')
   all_trs = tbody.find_elements(By.TAG_NAME, 'tr')
   
   next_pages_links = []

   
   for i in range(len(all_trs)):
      tr  = all_trs[i]
      tds = tr.find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')
      next_pages_links.append(tds)
   
   print('\n all links: ', next_pages_links)

   for i in range(len(next_pages_links)):
      links = next_pages_links[i]
      print('\n', links)
      driver.get(links)

      card_body = driver.find_element(By.CLASS_NAME, 'card-body')

      name  = card_body.find_element(By.CLASS_NAME, 'card-title').text
      email = card_body.find_element(By.TAG_NAME, 'p').text
      others = card_body.find_element(By.CLASS_NAME, 'text-muted').text 

      print(f'\n Name: {name} Email: {email} others: {others}')
      time.sleep(5)
      driver.find_element(By.XPATH, '/html/body/div/button/a').click()

      driver.close()
   

# news_app_scrappers()



def my_amazon_data():
   url = 'https://www.naukri.com/walkin-jobs?src=gnbjobs_homepage_srch&jobTypeFilter=6&cityTypeGid=9508'

   driver = webdriver.Chrome()
   driver.get(url)
   all_cards = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[2]')
   print(all_cards.text)

   
   driver.close()

# my_amazon_data()



class QuotesDriver:

   def __init__(self):
      self.driver = webdriver.Chrome()
   
   def get_url_data(self, url):
      """Get target url data as driver obj"""

      try:
         web_page = self.driver.get(url=url)
      except:
         pass
      else:
         return web_page
   
   def data_extractor_from_driver(self):
      url = 'https://www.passiton.com/inspirational-quotes?page=2'
      page = self.get_url_data(url=url)

      print(page)


def quotes_driver():
   paths = 'C:/Users/HP/Desktop/AllCredentials/chromedriver.exe'

   driver = webdriver.Chrome(executable_path=paths)
   url = 'https://www.passiton.com/inspirational-quotes?page=2'

   driver.get(url) # driver 

   all_quotes = driver.find_element(By.ID, 'all_quotes')
   all_href = []

   for dv in all_quotes:
      href = dv.find_element(By.TAG_NAME, 'a').get_attribute('href')
      all_href.append(href)

      

   print(all_href)

   
   
   driver.close()

# quotes_driver()
