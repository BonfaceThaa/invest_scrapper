from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class at_least_n_elements_found(object):

    def __init__(self, locator, n):
        self.locator = locator
        self.n = n

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) >= self.n:
            return elements
        else:
            return False

DRIVER_PATH = '/home/shadowfox/.wdm/drivers/chromedriver/linux64/90.0.4430.24/chromedriver'

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver = webdriver.Chrome(DRIVER_PATH)
driver.get(url)

driver.implicitly_wait(10)

div_element = driver.find_element_by_class_name('infinite-scroll')
qoutes_locator = (By.CSS_SELECTOR, ".quote:not(.decode)")

nr_quotes = 0
while True:
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollHeight', div_element
    )

    try:
        all_quotes = WebDriverWait(driver, 3).until(
            at_least_n_elements_found(qoutes_locator, nr_quotes + 1)
        )
    except TimeoutException as e:
        print("...done!")
        break

    nr_quotes = len(all_quotes)
    print("...now seing, nr", nr_quotes, "qoutes")

print(len(all_quotes), 'qourtes found\n')
for qoute in all_quotes:
    print(qoute.text)

input('Press ENTER to close the automated browser')
driver.quit()
