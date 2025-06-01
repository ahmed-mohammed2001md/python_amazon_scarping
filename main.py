
from scraper.fetch_data import Fetch

if __name__ == "__main__":

    # first thing we want to get the urls from the user
    urls = []
    while True:
        url = input('write the urls(if done press enter with empty value) : ')

        if url:
            urls.append(url.strip())
        else:
            break

    # check if urls lists is not empty
    if urls:
        # if there are urls get the data
        for url in urls:
            product_data = Fetch.fetch(url)


    else:
        print('There is no value')

    pass