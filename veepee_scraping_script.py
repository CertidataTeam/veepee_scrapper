import time
import selenium
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import schedule

def scrape_and_store_data():
    
    username = "manel.rebhi@certideal.com"
    password = "123456789Ma*"
    print("Selenium Version:", selenium.__version__)
    print("webdriver Version:", webdriver.__version__)


    # Initialize the Chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=chrome_options)    
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


    # Head to the login page
    driver.get("https://www.veepee.fr/gr/authentication?openDoor=true&returnUrl=")
    time.sleep(1)
    
    cookies = driver.find_element(By.XPATH, "//button[text()='Continuer sans accepter']")
    driver.execute_script("arguments[0].click();", cookies)
    time.sleep(1)
    
   # driver.execute_script("window.localStorage.clear();")
   # driver.execute_script("window.sessionStorage.clear();")
   # driver.execute_script("window.location.reload();")
   # driver.delete_all_cookies()
             

    # Find the username and password input fields
    username_input = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
    password_input = driver.find_element(By.XPATH, "//*[@id=\"current-password\"]")

    # Send keys to the input fields
    username_input.send_keys(username)
    time.sleep(2)

    password_input.send_keys(password)
    time.sleep(2)

    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.delete_all_cookies()
    

    # Retrieve the values entered into the input fields
    entered_username = username_input.get_attribute("value")
    entered_password = password_input.get_attribute("value")

    print("Entered Username:", entered_username)
    print("Entered Password:", entered_password)

   

    time.sleep(6)
    # Execute JavaScript to click the login button
    login_button = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"loginBt\"]")))
    time.sleep(2)
    driver.execute_script("arguments[0].click();", login_button)
    time.sleep(3)

    print(driver.current_url)
    print(driver.title)

    try:
        cookies_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continuer sans accepter']")))
        cookies_button.click()
        print("Continuer sans accepter")
    except:
        print("No cookies notification found.")
    
    time.sleep(2)

    # Retrieve the page source
    page_source = driver.page_source

    time.sleep(2)

    # Save the page source to a file
    with open("page_source_veepee.html", "w", encoding="utf-8") as file:
        file.write(page_source)
   
    try:
        cookies_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continuer sans accepter']")))
        cookies_button.click()
        print("Continuer sans accepter")
    except:
        print("No cookies notification found.")
    

    # Define the base URL
    base_url ='https://www.veepee.fr/gr/find?Query.displayFacets=true&Query.value=iphone&Query.isSuggestion=true&UnisexCategory=%2337%3AL2%2F3708%2F3720%2F&Brand=Apple'
    driver.get(base_url)
    
    time.sleep(2)
    
    try:
        cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continuer sans accepter']")))
        cookies_button.click()
        print("Continuer sans accepter")
    except:
        print("No cookies notification found.")
    
    time.sleep(1)
    # Collect all product URLs on the base_url through scrolling
    product_urls = set()
    scroll_step = 500
    max_scrolls = 70
    
    # Retrieve the page source
    page_source = driver.page_source

    # Save the page source to a file
    with open("page_source_veepee_all_prod.html", "w", encoding="utf-8") as file:
        file.write(page_source)

    for scroll_count in range(max_scrolls):
        driver.execute_script(f"window.scrollBy(0, {scroll_step});")

        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'a[data-testid="product-description"]')))
        except Exception as e:
            print(f"Error waiting for product description elements: {e}")

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        item_elements = soup.find_all('a', {'data-testid': 'product-description'})

        for item_element in item_elements:
            href = item_element['href']                       
            product_urls.add(href)

    print(len(product_urls))
#     product_urls =['https://www.veepee.fr/gr/product/863770/64984986?searchResultAccess=true']

    items = []

    # For each URL, visit the page and extract span texts under the specified div
    for href in product_urls:

        driver.get(href)
        print(driver.current_url)
        time.sleep(2)
        try:
            try:
                cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continuer sans accepter']")))
                cookies_button.click()
                print("Continuer sans accepter")
            except:
                print("No cookies notification found.")
 
            time.sleep(1)
        
            button =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"__next\"]/div/div/div/div/div[2]/button")))
                
            button.click()
            
            time.sleep(2)
            
            #new_window_page_source = driver.page_source

            # Get the page source of the pop-up window
            popup_page_source = driver.page_source

            # Use BeautifulSoup to parse the HTML of the pop-up window
            soup_product = BeautifulSoup(popup_page_source, 'html.parser')

            # Find product details
            products_details = soup_product.find_all('label', class_='sc-ecPEgm ePrhxD styles__Radio-groot__sc-5a63e5d7-1 cQdZlv')

            product_name = soup_product.find('h1').get_text(strip=True)

            for product in products_details:
                span_elements = product.find_all('span', class_='sc-gdyeKB jpBcur')
                all_span = [span.get_text(strip=True) for span in span_elements]

                if all_span:
                     capacity = all_span[0].split('-')[0]
                     state_and_price = all_span[0].split('-')[1]

                    # Find the index where the state ends and the price begins
                     for i in range(len(state_and_price)):
                        if state_and_price[i].isdigit():
                           state_end_index = i
                           break

                    # Extract state and price using the state_end_index
                     state__ = state_and_price[:state_end_index]
                     price__ = state_and_price[state_end_index:]


                     print("Product :")
                     print(href)
                     print(product_name)
                     print(capacity)
                     print(state__)
                     print(price__)
    
                     items.append({'href': href,'title':product_name,  'capacity':capacity,'state': state__,'price': price__})
                else:
                     print("No product details found.")


            # Switch back to the main window
            driver.switch_to.window(driver.window_handles[0])
            
        except NoSuchElementException:
            print("Button not found on this page. Skipping...")

    driver.quit()

    return items


def scrape_and_save():
    # Call your function to scrape and store data
    scraped_items = scrape_and_store_data()
    
    # Save the scraped data to a JSON file
    with open('veepee_prices.json', 'w') as json_file:
        json.dump(scraped_items, json_file)
        
# Schedule the script to run every day at 9 AM
#schedule.every().day.at("15:05").do(scrape_and_save)

while True:
    scrape_and_save()
    # Run pending scheduled tasks
    #schedule.run_pending()
    
    time.sleep(60)  


