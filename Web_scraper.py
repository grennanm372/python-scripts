from bs4 import BeautifulSoup
import requests
import os.path
from html.parser import HTMLParser
from html.entities import name2codepoint
import html2text
import urllib3

#file path
save_path = r"C:\Users\Morgan\Desktop\Python Scripts\Web Scraper"
file_name = "mass_of_urls.csv"
file_name2 = "raw_html.html"
UrlName = os.path.join(save_path, file_name)
raw_HTML = os.path.join(save_path, file_name2)

#Ask the user for the input URL to scrape the data from
url = input('Enter a website to extract the links from: ')

r = requests.get(url)       #Request data from the server using the GET protocol

data = r.text     #Convert the raw response to text to retrieve the data

soup = BeautifulSoup(r.content, features='lxml')    #Use the Python HTML Parser, to pull data out of the HTML file

#erase existing content in file
print("Erasing existing data.")
f = open(UrlName, 'a')
f.truncate(0)
f = open(raw_HTML, 'a')
f.truncate(0)
print("Erase complete.")

#print(h.handle(data))

list = ''   #Create an empty list to store the links in
#Get all the links from <a> tags with attribute href, and store it in lists variable
for link in soup.find_all('a'): 
        list += link.get('href') + '\n'
        f = open(UrlName, 'a')
f.write(list)
f.close()

for url in list:
        if url.startswith('https://') or url.startswith('http://'):
                r = requests.get(url)
                soup = BeautifulSoup(r.content, features="lxml")
                html_from_site = soup.get_text()
                html_from_site.strip()
                print(data)
        else:
                print("Skipped", url)

print( "Returned: ", len(list), "results. ") #print amount of results at end of process
print("Process complete.")


















