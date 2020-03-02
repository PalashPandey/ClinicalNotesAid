import PyPDF2 
import os
import requests
import bs4 as bs

# Relative File paths 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/documents/'

# creating a pdf file object 

pdfFileObj = open('C:\\Users\\pxp142\\Documents\\NoteAid\\myproject\\media\\documents\\SampleWriteUp.pdf' , 'rb') 

# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

page2 = pdfReader.getPage(0) 
# print(page2.extractText()) 

url_query = page2.extractText().replace(' ', '+')
response = requests.get('http://www.clinicalnotesaid.org/emrreadability/notesaidresults.uwm?emr_text=' + url_query)

notesparser = bs.BeautifulSoup(response.text , 'html.parser')

# print( len(notesparser.find_all('div' , attrs={'style' : 'float:center; width: 60%;'} ) ))
print( notesparser.find('div' , attrs={'style' : 'float:center; width: 60%;'} )  )
