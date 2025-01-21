import uuid
import requests
from datetime import datetime
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def fetch_twitter_trends(username, password):
    # Set up WebDriver with detach option
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)    
    try:
        driver.get("https://x.com/login")
        time.sleep(3)  
        username_input = driver.find_element(By.NAME, "text")
        username_input.send_keys(username)
        username_input.send_keys(Keys.RETURN)
        time.sleep(2)     
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)   
        trends_section = driver.find_element(By.XPATH, "//section[contains(@aria-labelledby, 'accessible-list')]")
        trends = trends_section.find_elements(By.XPATH, "//div[contains(@data-testid, 'trend')]")
        top_trends = [trend.text for trend in trends[:5]]
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        ip_address = requests.get("https://api.ipify.org").text
        unique_id = str(uuid.uuid4())
        trend_data = {
            "unique_id": unique_id,
            "trend1": top_trends[0] if len(top_trends) > 0 else None,
            "trend2": top_trends[1] if len(top_trends) > 1 else None,
            "trend3": top_trends[2] if len(top_trends) > 2 else None,
            "trend4": top_trends[3] if len(top_trends) > 3 else None,
            "trend5": top_trends[4] if len(top_trends) > 4 else None,
            "date_time": end_time,
            "ip_address": ip_address
        }
        with open("results.json", "w") as json_file:
            json.dump(trend_data, json_file, indent=4)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = "Flash7672827676"
    password = "flashyflash@213"
    fetch_twitter_trends(username, password)
