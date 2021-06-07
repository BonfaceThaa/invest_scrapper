from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

DRIVER_PATH = '/home/shadowfox/.wdm/drivers/chromedriver/linux64/90.0.4430.24/chromedriver'

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver = webdriver.Chrome(DRIVER_PATH)
driver.get(url)
# driver.implicitly_wait(10)

quote_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".quote:not(.decode)")
    )
)

# for quote in driver.find_elements_by_class_name('quote'):
#     print(quote.text)

for quote in quote_elements:
    print(quote.text)

input('Press ENTER to close the automated browser')
driver.quit()