
import gspread
import pandas as pd
import requests, json, os
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials



# google sheet handler
class GoogleSheetHandler:
   
   # constructor
   def __init__(self, credFile, sheetName):
      self.credFile = credFile
      self.sheetName= sheetName
      self.client   = None
      self.sheet    = None

      self.authorizeClient()

   # client authorization
   def authorizeClient(self):
      
      # google scopes here define access modes
      scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
               "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
      
      if os.path.isfile(self.credFile): # if file exist on given path
         credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credFile, scopes=scope)

            
         try:
            client      = gspread.authorize(credentials=credentials)
            
         except:
            print('\n Client Authorization fialed')
            pass

         else:
            self.client = client   # saving authorized client for further use
            self.openGsheet() # opening google sheet here

            print('\n Congrats Client Authorized Successfully')

      else:
         print('\n Errro: User Credential file does not found ' )
   
   # opening here  GoogleSheet
   def openGsheet(self):
      sheet = None

      try:
         sheet  = self.client.open(title=self.sheetName).sheet1

      except:
         print('Exception while opening google sheet ')

      else:
         self.sheet = sheet # saving obj

         print('Google Sheet Opened Successfully')
   
   def gSheetReader(self):
      print(self.sheet.col_count)
      pass
   
   def gSheetWtitter(self):
      """Store API response data into google sheet"""
      if self.client:
         print('\n Start Writting into Google Sheet')

                  
         sheetName = 'Companies API Data' # sheet name
         sheetKey  = '1Cn-ubhkcRZi51k0rZdGVwmhSyulY19Q-5tSDRSE5kfc' # sheetKey
         wrkSheetName = 'Sheet1' # sheetname
         cellOfStart  = 'A1'  # cell start

         scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
               "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
         
         credentials = ServiceAccountCredentials.from_json_keyfile_name(self.userCreds, scopes=scope)

         api_data = None # here please put data
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

gSheetName        = 'Companies API Data'
gSheetCredentials = 'C:/Users/bhole/OneDrive/Desktop/Credentials/googleSheetCredentials.json' # credential file


sheetHandler = GoogleSheetHandler(credFile=gSheetCredentials, sheetName=gSheetName)

sheetHandler.gSheetReader()
   
   