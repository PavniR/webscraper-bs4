import requests
from bs4 import BeautifulSoup

#print("all pips are imported!")

for year in range(2021,2026):               #prints 4 lists for 5 years  
    url = f"https://www.imdb.com/search/title/?release_date={year}-01-01,{year}-12-31&sort=moviemeter,asc"  #url of site to scrape
    headers = {"User-Agent": "Mozilla/5.0" }         #since IMDb does not allow scraping so we are tricking it into thinking a browser asked for access 

    page = requests.get(url, headers=headers) #will send request and make a response object 

    soup = BeautifulSoup(page.text, "html.parser")  #create a soup object from the response text
    #BeautifulSoup(page.text, "html.parser") will parse the response object and return raw html

    movie_titles = soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced")  #filters required html data from soup object by finding where the titles are stored 
    
    print(f"\nTop movies for the year: {year}")
    for titles in movie_titles:                            #looping through each one of the tags
        movie = titles.get_text().strip()                  #get_text() to remove tags from html and get only titles, strip() to remove extra spaces 
        print(movie)                                       #print the list! 

print("here's list of top movies from last 5 years!")