from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd

def simple_driver_to_login_at_pythonanywhere():
      
   driver = webdriver.Chrome()
   url = 'https://www.pythonanywhere.com/login/'
   driver.get(url)

   # driver will wait for 10 second let all contetn loads
   # driver.implicitly_wait(10) 


   # finding user-name field
   try:
      driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/form/p[1]/input').send_keys('scrappers')
   except:
      print('No username is found')

   # user password
   try:
      driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/form/p[2]/input').send_keys('databasereal1437@')
   except:
      print('No password is found')

   # find login button
   try:
      driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/form/button').click()
   except:
      print('No click button found')
      pass

# simple_driver_to_login_at_pythonanywhere()

def find_element_by_id():
   url = 'https://www.geeksforgeeks.org/find_element_by_id-driver-method-selenium-python/'
   
   driver = webdriver.Chrome()
   driver.get(url=url)

   try:
      elm = driver.find_element(By.ID,"openInApp-modal")
   except:
      print('No elm found')
   else:
      print(elm)
# find_element_by_id()


def find_elm_with_class():

   driver = webdriver.Chrome()
   url = 'https://www.geeksforgeeks.org/find_element_by_id-driver-method-selenium-python/'

   driver.get(url=url)

   try:
      elm = driver.find_element(By.CLASS_NAME, 'article--viewer_content')
   except:
      print('No elm with class')
   else:
      print('\nclass: obj', elm)


# find_elm_with_class()

def find_elm_with_links():

   driver = webdriver.Chrome()
   url = 'https://www.geeksforgeeks.org/find_element_by_link_text-driver-method-selenium-python/?ref=rp'

   driver.get(url)

   try:
      elm = driver.find_element_by_link_text('find_element_by_css_selector')
   except:
      print('not found')
      pass
   else:
      print('elm found')
      driver.get(url=elm)

# find_elm_with_links()


def login_driver():
   # target url
   url = 'https://www.pythonanywhere.com/login/'
   chrome_opitions = Options()

   chrome_opitions.page_load_strategy = 'normal'            # it will wait till page complete load that is normal
   chrome_opitions.add_experimental_option('detach', True)  # keep browser open


   # chrome driver
   driver = webdriver.Chrome(chrome_options=chrome_opitions) 

   # making request to server
   driver.get(url)

   username = driver.find_element(By.ID, "id_auth-username")
   password = driver.find_element(By.ID, "id_auth-password")

   print(username, password)

   username.send_keys('your_user_name')  # provinding user-name
   password.send_keys('your_password_here') # provinding password
   login_btn  = driver.find_element(By.ID, 'id_next').click()

   

   
   # closing opened tab
   # driver.close()

# login_driver()


def youtube_data2():

   # url = 'https://www.youtube.com/@worthwebscraping-mike6107'
   
   url = 'https://www.youtube.com/@JohnWatsonRooney'
   
   chrome_options = Options()

   # page load stratgey
   # chrome_options.page_load_strategy = 'normal'

   # keep browser open
   chrome_options.add_experimental_option('detach', True)

   # making web-driver
   driver = webdriver.Chrome(chrome_options=chrome_options)

   # makeing requests
   driver.get(url)

   videos = driver.find_elements(By.CLASS_NAME, "style-scope yt-horizontal-list-renderer")  

   
   videos_list = []

   for video in videos:
      vid_items = {}
      # title = video.find_element(By.ID, 'video-title').text
      title  = video.find_element(By.XPATH, './/*[@id="video-title"]').text
      vid_items['title'] = title

      try:
         # views = video.find_element(By.ID, "metadata-line").find_element(By.TAG_NAME, "span").text
         views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
      except:
         pass
      else:
         vid_items['no_views'] = views

      
      try: # #metadata-line > span:nth-child(2)
         # days = video.find_element_by_css_selector('span:nth-child(2)').text
         days = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
      except:
         pass
      else:
         vid_items['posted'] = days
      
      videos_list.append(vid_items)

   df = pd.DataFrame(data = videos_list)

   print(df.head())
      
   driver.close()
   driver.quit()

# youtube_data2()





