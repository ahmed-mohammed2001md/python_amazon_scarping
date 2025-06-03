from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time, random
import scraper.configer as configer


class Fetch:

    def fetch(url):
        '''This method get the html source 
        
        Args:
            url (str) : the url of the amazon product
        '''

        # Configure Chrome options with headers
        chrome_options = Options()

        # Add headers and other settings to mimic a real browser
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
        chrome_options.add_argument("--accept-language=en-US,en;q=0.9")
        chrome_options.add_argument("--referer=https://www.google.com/")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # Disable the "Chrome is being controlled by automated test software" notification
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        service = webdriver.ChromeService(executable_path = './chromedriver.exe')

        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)

        # check if there a capcha or not, and if it is there and solved refresh the page
        if Fetch.handle_captcha(driver):
            # Refresh page data after solving
            driver.refresh()

        # Get the page source
        page_source = driver.page_source
        
        time.sleep(random.uniform(configer.MIN_SLEEP_DELAY, configer.MAX_SLEEP_DELAY))

        # the soup
        soup = BeautifulSoup(page_source, 'html.parser')

        driver.quit()

        return soup


    def handle_captcha(driver):
        '''this method check if capcha is there or not '''
        try:
            # Check if CAPTCHA is present
            captcha = WebDriverWait(driver, random.uniform(configer.MIN_SLEEP_DELAY, configer.MAX_SLEEP_DELAY)).until(EC.presence_of_element_located((By.ID, "captchacharacters")))
            
            if captcha:
                print("CAPTCHA detected - please solve it manually")
                input("Press ENTER after solving CAPTCHA...")
                
                # Wait for CAPTCHA to disappear
                WebDriverWait(driver, random.uniform(configer.MIN_CAPTCHA_DELAY, configer.MAX_CAPTCHA_DELAY)).until(
                    EC.invisibility_of_element_located((By.ID, "captchacharacters")))
                
                return True
        except:
            return False
