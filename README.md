## 📌 Overview
This is an Amazon product scraper built with Selenium that allows users to collect product data by providing Amazon URLs. The tool is designed for educational purposes to demonstrate web scraping techniques.

## ✨ Features
URL Input System: Users can input multiple Amazon product URLs one by one

Flexible Execution: Starts scraping when user presses Enter with empty input

Captcha Handling: Pauses execution when captcha is detected and waits for manual resolution

CSV Output: Saves all scraped data in outputs/output.csv file

Append Mode: New scraped data gets appended to the existing CSV file

Educational Focus: Designed to help learn web scraping concepts

# 🛠 Requirements
Python 3.x

Selenium

WebDriver for your preferred browser (Chrome recommended)

Required Python packages (install via pip install -r requirements.txt)

## 🚀 How to Use
Run the scraper script

Enter Amazon product URLs one by line

When finished entering URLs, press Enter with empty input to start scraping

If captcha appears:

Solve the captcha manually in the browser

Press Enter in the command line to continue

Collected data will be saved in outputs/output.csv

## ⚠ Important Notes
This tool is for educational purposes only

Respect Amazon's Terms of Service and robots.txt

Use appropriate delays between requests to avoid IP blocking

The developer is not responsible for any misuse of this tool

📜 License
This project is open-source and available for educational use. Commercial use is prohibited.

