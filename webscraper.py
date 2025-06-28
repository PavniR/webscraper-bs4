import requests
from bs4 import BeautifulSoup

#print("all pips are imported!")

url = "https://www.imdb.com/search/title/?release_date=2025-01-01,2025-06-21&sort=moviemeter,asc"  #url of site to scrape

headers = {
    "User-Agent": "Mozilla/5.0"           #since IMDb does not allow scraping so we are tricking it into thinking a browser asked for access 
}
page = requests.get(url, headers=headers) #will send request and make a response object 

#BeautifulSoup(page.text, "html.parser") will parse the response object and return raw html 
soup = BeautifulSoup(page.text, "html.parser")  #create a soup object from the response text

#print(soup.prettify())  

movie_titles = soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced")  #filters required html data from soup object by finding where the titles are stored 

#print(movie_titles)

for titles in movie_titles:                            #looping through each one of the tags
    movie = titles.get_text().strip()                  #get_text() to remove tags from html and get only titles, strip() to remove extra spaces 
    print(movie)                                       #print the list! 

print("here's list of top 25 movies in 2025!")

#note: however, the actual webpage with url shows 50 movies but we get a list of only 25 because we are using requests which get us static html
#The full list of 50 movies might be loaded dynamically with JavaScript in your browser, to dynamically scrape data, use selenium webdriver 
