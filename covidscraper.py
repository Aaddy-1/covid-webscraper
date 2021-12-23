#Importing modules
#Import Requests for querying url
#Import BeautifulSoup for parsing html content
#Import CSV for writing to csv file
import requests
from bs4 import BeautifulSoup
import csv

#URL from which I scraped the data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

#Getting URL html content by using requests
#Soup variable for storing parsed html data from the page
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


#Declaring empty data array for storing the sraped data
data = []

# soup.find_all('td') will scrape every row in the table
#iter() creates an iterable object
data_iterator = iter(soup.find_all('tr'))

#Creates data array using the parsed data
for i in data_iterator:
    data.append(i.text.replace('\n', ' ').split())
print(data) 

#Writes the data to the csv file
with open(r'C:\Users\sharm\Desktop\Programming\Python\covid-data.csv', 'w', encoding="mbcs") as csvwriterfile:

    csv_writer = csv.writer(csvwriterfile) 
    csv_writer.writerows(data)

csvwriterfile.close()