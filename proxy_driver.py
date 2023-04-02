
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getss(url):


   # chrome_options = webdriver.ChromeOptions()
   # chrome_options.add_experimental_option('detach', True)
   # chrome_options.add_argument('--proxy-server=%s' % PROXY)
   # chrome = webdriver.Chrome(chrome_options=chrome_options)
   # chrome.get(url)
   pass



URL = 'http://google.com'

getss(URL)
URL = 'http://scrappers.pythonanywhere.com/flipkart-products/scrapper/'

class WebDriver:

   def __init__(self):
      self.driver = webdriver.Chrome()

   
   def web_page(self,url, proxy=None,):
      chrome_options = Options()
      chrome_options.page_lcdoad_strategy = 'normal'
      chrome_options.add_experimental_option('detach', True)
      chrome_options.add_argument('--proxy-server=%s'%proxy)
      driver = webdriver.Chrome(chrome_options=chrome_options)
      driver.get(url)

      print(driver.title)

URL = 'http://scrappers.pythonanywhere.com/flipkart-products/scrapper/'

driver = WebDriver()

driver.web_page(URL)