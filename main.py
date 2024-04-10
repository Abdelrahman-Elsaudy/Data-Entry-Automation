from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --------------------------- BeautifulSoup for Zillow ---------------------------#


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_content = response.text
soup = BeautifulSoup(zillow_content, "html.parser")

addresses_tag = soup.select("address[data-test='property-card-addr']")
addresses = [address.getText().replace("\n", "").strip() for address in addresses_tag]

prices_tags = soup.select("span[data-test='property-card-price']")
prices = [price.getText().replace("/mo", "").replace("+", "").
          replace(" 1bd", "").replace(" 1 bd", "")
          for price in prices_tags]

links_tags = soup.select("a[class='property-card-link']")
links = [link.get("href") for link in links_tags]


# --------------------------- Selenium for Google Forms ---------------------------#


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# The link below is going to change according to your own Google Form.
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeHXsqCSy4XVFuFPLc3oPw1t9TSpy33Guc5lliOAN3ZZm4_Pw/viewform?usp=pp_url")


for i in range(len(prices)):
    time.sleep(4)

    address_entry = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div'
                                        '/div[1]/input')
    price_entry = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div'
                                      '/div[1]/input')
    link_entry = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div'
                                     '/div[1]/input')

    address_entry.send_keys(addresses[i])
    price_entry.send_keys(prices[i])
    link_entry.send_keys(links[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
    time.sleep(3)

    # The link below is going to change also according to your own Google Form.
    another = driver.find_element(By.CSS_SELECTOR, 'a[href="https://docs.google.com/forms/d/e/1FAIpQLSeHXsqCSy4XVF'
                                                   'uFPLc3oPw1t9TSpy33Guc5lliOAN3ZZm4_Pw/viewform?usp=form_confirm"]')
    another.click()
