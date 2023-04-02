from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

class  NaukriDriver:

    
   def __init__(self, target_url:str):
      self.url = target_url
      self.driver = None

   def get_driver2(self):
      path = 'C:/Users/HP/Desktop/AllCredentials/chromedriver.exe'

      chrome_options = Options()
      # load browser normaly
      chrome_options.page_load_strategy = 'normal'
       

      try:
         driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
      except:
         print('\nException while making driver')
      else:
         print('\nDriver Create Your Ready Go')
   
   def get_driver(self, url=None):

      path = 'C:/Users/HP/Desktop/AllCredentials/chromedriver.exe'

      if not url:
         url = self.url

      chrome_options = Options()
      
      # load browser normaly
      chrome_options.page_load_strategy = 'normal'
       
       # keep browser open
      # chrome_options.add_experimental_option('detach' ,True)

      driver = webdriver.Chrome(executable_path=path,  chrome_options=chrome_options)

      driver.get(url) 

      pro_title = []
      pro_price = []
      pro_rating = []
      pro_reviews = []


      def product_extractor():
         cards = driver.find_element(By.ID, 'card_products')

         for i in range(1,8):
            product = cards.find_element(By.XPATH, f'//*[@id="card_products"]/div[{i}]')
            title = product.find_element(By.XPATH, './div/div/div[2]/div/h4').text
            price = product.find_element(By.XPATH, './div/div/div[2]/div/p[1]/strong').text[33:40].replace(',','')
            all = product.find_element(By.XPATH, './div/div/div[2]/div/p[2]').text
            rating = all[8:11]
            no_rewievs = all[22:-9]

            pro_price.append(price)
            pro_rating.append(rating)
            pro_title.append(title)
            pro_reviews.append(no_rewievs)


            time.sleep(3)

      # product_extractor()

      def next_page():
            
         for i in range(3):
            print('\n \n \n')
            driver.find_element(By.XPATH, '//*[@id="card_products"]/nav[1]/ul/li[4]/a').click()
            product_extractor()
            time.sleep(2)
      
      # next_page()

      def add_new_product():
         url = 'http://127.0.0.1:8000/naukri/add-product/'

         for i in range(len(pro_title)):

            driver.get(url)

            title = driver.find_element(By.XPATH, '//*[@id="id_title"]').send_keys(pro_title[i])
            price = driver.find_element(By.XPATH, '//*[@id="id_price"]').send_keys(pro_price[i])
            rating = driver.find_element(By.XPATH, '//*[@id="id_rating"]').send_keys(pro_rating[i])
            reviews = driver.find_element(By.XPATH, '//*[@id="id_reviews"]').send_keys(pro_reviews[i])
            btn = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/form/input[2]')
            btn.click()
            time.sleep(3)
     
      # add_new_product()
      global post_links

      post_links = []

      def get_post_links():

         rows = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div')

         for i in range(1,11): # '/html/body/div[2]/div[2]/div/div[2]'
            jobs = rows.find_element(By.XPATH, f'/html/body/div[2]/div[2]/div/div[{i}]')
            links = jobs.find_element(By.XPATH, './div/h1/a').get_attribute('href')
            post_links.append(links)
         time.sleep(3)


      get_post_links()
      print('\n', len(post_links))

      def details_page_extractor():
         print('\n ')
         title = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/h1').text[7:]
         price = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/p[1]').text[7:]
         rating = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/p[2]').text[7:]
         reviews = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/p[3]').text[8:]

         print(f'\n \n {title} {price} {rating} {reviews}')

      def pages():

         for i in range(len(post_links)):
            print(f'\n iterations no: {i+1} ')

            
            try:
               links = post_links[i]
            except:
               print(f'\n \n Exception while getting links {i} ')
            
            else:
               print('\n link found ', links)
               

               try:
                  driver.get(links)
               except:
                  print(f'\n \n Exception while clicking {i} ')
               else:
                  details_page_extractor()
                  print(f'\nLinks was clicked successfuly times: {i} ')
               time.sleep(3)



            time.sleep(2)

         
         print('\n  \n Out of Loop', )
      
      pages()
     
    

      print('\n closing window start ')
      time.sleep(4)


      driver.quit()



# url = 'http://127.0.0.1:8000/flipkart-products/scrapper/'
# url = 'http://127.0.0.1:8000/naukri/product-list/'
# # url = 'http://127.0.0.1:8000/naukri/product-details/33/'

# url = 'http://127.0.0.1:8000/naukri/product-list/'


# p1 = NaukriDriver(target_url=url)
# driver.get_driver()
# driver = p1.get_driver2()
# driver.get(url)

# price = (f'Total Price: 14,999 Actual Price: 9,299 Discount Percentage: 38% off ')
# price = 'Rating: 4.3  Reviews: 1,95,030 Ratings  '
# print(price[22:-9])


