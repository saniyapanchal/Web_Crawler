import requests
from bs4 import BeautifulSoup

def crawl_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = extract_relevant_data(soup)

    for link in soup.find_all('a', href=True):
        next_url = link['href']
        crawl_page(next_url)

    return data

def extract_relevant_data(soup):
    return {
        'title': soup.title.text,
        'paragraphs': soup.find_all('p'),
    }
