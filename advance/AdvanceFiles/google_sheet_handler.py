import gspread
import pandas as pd
import requests, json, os
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials


api_urls = 'http://yadav222.pythonanywhere.com/api/companies/'                        # api endpoints
cred_file = 'C:/Users/bhole/OneDrive/Desktop/Credentials/googleSheetCredentials.json' # credential file


# API handler
class APIHandler:
    
   # Constructor
   def __init__(self, api_url):
      self.api_url     = api_url
      self.api_data    = None
      self.get_api_data()  # setting data

   # getting api data
   def get_api_data(self):
      response = None
      headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

      try:
         response = requests.get(url=api_urls, headers=headers)
      except:
         print('\n Exception while getting data from api')
      else:
         if response.status_code == 200:
            self.api_data = response.json()

# googleSheet handler to store api data into google sheet
class GoogleSheetHandler:
   
   # Constructor
   def __init__(self, credsFile:str):
      self.userCreds  = credsFile
      self.client     = None
      self.sheet      = None
      self.authorizeClient() # performing client authentication
   
   def authorizeClient(self):
      
      # google scopes here define access modes
      scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
               "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
      
      if os.path.isfile(self.userCreds): # if file exist on given path
         credentials = ServiceAccountCredentials.from_json_keyfile_name(self.userCreds, scopes=scope)

            
         try:
            client      = gspread.authorize(credentials=credentials)
            
         except:
            print('\n Client Authorization fialed')
            pass

         else:
            self.client = client
            print('\n Client Authorized')

      else:
         print('\n Errro: User Credential file does not found ' )
   
   def openGsheet(self, sheetName:str):
      sheet = None

      try:
         sheet  = self.client.open(title=sheetName).sheet1
      except:
         print('Exception while opening google sheet ')
      else:
         self.sheet = sheet
         
         print('Google Sheet Opened Successfully')
   
   def gSheetWtitter(self):
      """Store API response data into google sheet"""
      if self.client:
         print('\n Start Writting into Google Sheet')

                  
         sheetName = 'Companies API Data'
         sheetKey  = '1Cn-ubhkcRZi51k0rZdGVwmhSyulY19Q-5tSDRSE5kfc'
         wrkSheetName = 'Sheet1'
         cellOfStart  = 'A1'

         scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
               "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
         
         credentials = ServiceAccountCredentials.from_json_keyfile_name(self.userCreds, scopes=scope)

         api_data = apis.api_data
         df       = pd.DataFrame(api_data)

         if not api_data:
            pass
         else:
                     
            try:
               d2g.upload(
               df,
               sheetKey,
               credentials=credentials, 
               col_names=True,
               row_names=False,
               start_cell=cellOfStart,
               clean=True)
            except:
               print('/n Exception while writting data into google sheet')
            
            else:
               print('\n Data successfully written in Google Sheet')
               print('\n All Operation Perfomed Successfully')


# getting api data from api target url
apis = APIHandler(api_url=api_urls) # 


# googlesheet obj 
gSheet = GoogleSheetHandler(credsFile=cred_file)

gSheet.gSheetWtitter()   #


# print(apis.api_data)