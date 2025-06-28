# Movies Scraper using BeautifulSoup 

This repo contains two **Python Scripts** which scrape IMDb for movie data using `requests` and `BeautifulSoup`. Each script demonstrates how to fetch and parse movie listings based on different time ranges. 

## Project Structure
- webscraper.py #scrapes top movies from JUN-JUN 2025
- scraper2.py #scrapes top movies for each year from 2021-25
- README.md #you're reading it right now

## Technologies Used

- Python 3
- `requests` module
- BeautifulSoup library (bs4)

## What These Scripts Do

### `webscraper.py`

- Scrapes top 25 movies released between January-June, 2025.
- Prints the list of movie titles to console. 

### `scraper2.py`

- loops through the years **2021-2025**.
- for each year, it scrapes top 25 movies released between **January-June**.


## Setup
1. Clone the Repository
git clone https://github.com/PavniR/webscraper-bs4.git
run the command to navigate through folder: cd webscraper-bs4

2. Install Required Libraries
make sure python 3 is installed then install the libraries through this command: pip install beautifulsoup4 requests

3. Run a Script 
command: python webscraper.py
or
commmand: python scraper2.py

## Static Scraping
Through these scripts, we can get only top 25 movies for the mentioned time range. This is because the initial 25 movie listings on the search results page are embedded in **static HTML response**. This allows `requets` and `BeautifulSoup` to extract data, but only partially. 
- `requests` is a Python Library that sends a simple **HTTP request** to a server and retrieves raw HTML. 
- `bs4` then parses the static HTML and lets you navigate and extract data through it.

However, many modern websites use JavaScript to load or update content after the initial HTML is sent (which most modern sites like IMDb, YouTube, Twitter do), `requests` + `bs4` can’t see that extra content because-

- `requests` doesn't execute JavaScript, and
- `bs4` can only see the initial, static HTML, not the dynamic content added later.

As a result, `requests` + `bs4` can't access data beyond what's already in the raw HTML — such as the rest of the movie listings beyond the first 25.

This project uses `requests` + `BeautifulSoup` for static scraping, which is lightweight and efficient, but limited to preloaded content.

To scrape dynamically loaded content, we need tools that can simulate a browser and execute JavaScript — such as Selenium or Playwright.



For that, I have created a separate script for **Dynamic Scraping** using Selenium Webdriver:
🔗 [WebScraper using Selenium Webdriver](https://github.com/PavniR/webscraper-selenium)


## Disclaimer
- this is for educational purposes only
- IMDb's content is protected, and scraping it should comply with their terms of service.

## Future Improvements 
- save results to JSON/CSV file.
- Add error handling for invalid responses.
- Extend scraping to include ratings, genres, or descriptions.

## Author

Pavni Rastogi