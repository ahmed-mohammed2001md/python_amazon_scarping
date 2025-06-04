## 📌 Overview
This is an Amazon product scraper built with Selenium that allows users to collect product data by providing Amazon URLs. The tool is designed for educational purposes to demonstrate web scraping techniques.

## ✨ Features
<ul>
<li>URL Input System: Users can input multiple Amazon product URLs one by one</li>

<li>Flexible Execution: Starts scraping when user presses Enter with empty input</li>

<li>Captcha Handling: Pauses execution when captcha is detected and waits for manual resolution</li>

<li>CSV Output: Saves all scraped data in outputs/output.csv file</li>

<li>Append Mode: New scraped data gets appended to the existing CSV file</li>

<li>Educational Focus: Designed to help learn web scraping concepts</li>
</ul>

## 🛠 Requirements

<ul>
<li>Python 3.x</li>

<li>Selenium</li>

<li>WebDriver for your preferred browser (Chrome recommended)</li>

<li>Required Python packages (install via pip install -r requirements.txt)</li>
</ul>

## 🚀 How to Use
<ol>
<li>Run the scraper script</li>

<li>Enter Amazon product URLs one by line</li>

<li>When finished entering URLs, press Enter with empty input to start scraping</li>

<li>If captcha appears:</li>


<ul>
<li>Solve the captcha manually in the browser</li>

<li>Press Enter in the command line to continue</li>
</ul>


<li>Collected data will be saved in outputs/output.csv</li>
</ol>

## ⚠ Important Notes

<ul>

<li>This tool is for educational purposes only</li>

<li>Respect Amazon's Terms of Service and robots.txt</li>

<li>Use appropriate delays between requests to avoid IP blocking</li>

The developer is not responsible for any misuse of this tool
</ul>
📜 License
This project is open-source and available for educational use. Commercial use is prohibited.

