# Data Entry Automation

---

- Combining both `BeautifulSoup` and `Selenium` to automate compiling a list for rental properties from 
[Zillow](https://www.zillow.com/) with certain defined features and write them on [Google forms](https://docs.google.com/forms/).

- Basically scrapping data from a website that looks like this:

![zillow](https://github.com/Abdelrahman-Elsaudy/Shopping-Price-Alert/assets/158151388/6cdc6ea8-b6f2-4763-9937-0ed2b166b124)

- To form a sheet that looks like this:

![sheets](https://github.com/Abdelrahman-Elsaudy/Shopping-Price-Alert/assets/158151388/add2ca27-e09f-4b85-9145-238ff7388b9d)

---

## Skills Practiced:

---

- Data collecting by web scrapping using `BeautifulSoup`.
- Data cleaning.
- Data entry automation using `Selenium`.


---

## Prerequisites:

---

- This code is written to work on a [Zillow's clone](https://appbrewery.github.io/Zillow-Clone/) website to guarantee its HTML doesn't change.
- At the beginning, we create a Google Form in which we will fill the questions wih the data we get, and this form is then
turned into a Google Sheet.

---
## How This Tool Works:

1. To form the above sheet, we need each property's address, rental price/month and links.
2. To do this we use `BeautifulSoup` to create 3 lists, one for addresses, one for prices and one for links:
```
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
```
3. After getting these three lists, and since each index in them represents a specific property, we iterate through them
to fill the Google Form and submit a response that represents each property.
```
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

    # The link below is going to change according to your own Google Form.
    another = driver.find_element(By.CSS_SELECTOR, 'a[href="https://docs.google.com/forms/d/e/1FAIpQLSeHXsqCSy4XVF'
                                                   'uFPLc3oPw1t9TSpy33Guc5lliOAN3ZZm4_Pw/viewform?usp=form_confirm"]')
    another.click()
```
4. After filling the Form with the responses, we press on the _Sheets_ icon to form the desired sheet.
![responses](https://github.com/Abdelrahman-Elsaudy/Shopping-Price-Alert/assets/158151388/d27239a7-866a-49eb-9998-be1408f85372)

---
_Credits to: 100-Days of Code Course on Udemy._