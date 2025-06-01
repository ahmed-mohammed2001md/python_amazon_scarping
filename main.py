
from scraper.fetch_data import Fetch
from scraper.process_data import Process
from bs4 import BeautifulSoup

if __name__ == "__main__":

    # first thing we want to get the urls from the user
    urls = []
    while True:
        url = input('write the urls(if done press enter with empty value) : ').strip()

        if url:
            urls.append(url)
        else:
            break

    # check if urls lists is not empty
    if urls:
        # if there are urls get the data
        for url in urls:

            product_data = Fetch.fetch(url)
            Process.product(product_data, url)

    else:
        print('There is no value')

    pass