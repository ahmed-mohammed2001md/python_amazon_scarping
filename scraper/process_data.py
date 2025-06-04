from bs4 import BeautifulSoup, Tag
import scraper.configer as configer
from scraper.save_data import Save

class Process:


    def product(product_data, url):
        '''
            This mehtod extact data from soup and save them as varibles
            Last this send data to Save class as CSV file

            Args:
                product_data : soup of page
                url : the url of the page for extract asin
        '''
                
        # single value
        url = url
        title = product_data.select_one(configer.TITLE).text.strip() if product_data.select_one(configer.TITLE) else None
        current_price = product_data.select_one(configer.CURRENT_PRICE).text.strip() if product_data.select_one(configer.CURRENT_PRICE) else None
        discount = product_data.select_one(configer.DISSCOUNT).text.strip() if product_data.select_one(configer.DISSCOUNT) else '0%' 
        list_price = product_data.select_one(configer.LIST_PRICE).text.strip() if product_data.select_one(configer.LIST_PRICE) else None
        rating = product_data.select_one(configer.RATING).text.strip() if product_data.select_one(configer.RATING) else None
        availability = product_data.select_one(configer.AVAILABILITY).text.strip() if product_data.select_one(configer.AVAILABILITY) else None
        reviews_count = product_data.select_one(configer.REVIEWS_COUNT).text.strip() if product_data.select_one(configer.REVIEWS_COUNT) else None
        seller = product_data.select_one(configer.SELLER).text.strip().replace('Visit the', '') if product_data.select_one(configer.SELLER) else None
        asin = configer.ASIN(url)


        # multiple choices
        colors = Process.handle_colors(product_data.select_one(configer.COLORS))
        styles = Process.handle_styles(product_data.select_one(configer.STYLES))
        sizes = Process.handle_sizes(product_data.select_one(configer.SIZES))

        full_data = {
            'Title': title,
            'Asin' : asin,
            'Current Price' : current_price,
            'Discount' : discount,
            'List Price' : list_price,
            'Rating' : rating,
            'Availability' : availability,
            'Reviews Count' : reviews_count,
            'Seller' : seller,
            'Colors' : colors,
            'Styles' : styles,
            'Sizes' : sizes,
            'Url' : url,

        }

        # send data to Save class to save them
        Save.csv(full_data)

        

    def handle_colors(colors):

        if colors:
            # remove navigablestring
            colors =  [child for child in colors if isinstance(child, Tag)]

            # the var will recive the data
            data = []

            try:
                for index, color in enumerate(colors):
                    
                    if color:
                        # get product colors and save them in
                        data.append(color.select_one(f'img').get('alt') if color.select_one(f'img').get('alt') else 'no color')
            except:
                pass

            finally:
                return data


    def handle_styles(styles):

        if styles:
            # remove navigablestring
            styles =  [child for child in styles if isinstance(child, Tag)]

            # the var will recive the data
            data = []

            try:
                for index, style in enumerate(styles):
                    try:
                        if style:
                            data.append(style.select_one(f'#style_name_{index}-announce').text.strip() if style.select_one(f'#style_name_{index}-announce') else 'no style')
                    except:
                        pass
            except:
                pass
            
            finally:
                return data


    def handle_sizes(sizes):

        # check if there sizes
        if sizes:

            # remove navigablestring
            sizes =  [child for child in sizes if isinstance(child, Tag)]

            # the var will recive the data
            data = []

            try:
                for index, size in enumerate(sizes):
                    try:
                        if size:
                            data.append(size.select_one(f'#size_name_{index}-announce').text.strip() if size.select_one(f'#size_name_{index}-announce') else 'no size')
                    except:
                        pass
            except:
                pass

            finally:
                return data
        



    