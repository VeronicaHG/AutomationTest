
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


PATH = '/Users/vhg/code/VeronicaHG/selenium/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://www.haba-play.com/en_DE")

driver.set_window_size(1440, 813)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

my_element = driver.find_element_by_id('onetrust-accept-btn-handler')
my_element.click()

#add first element
driver.find_element(By.ID, "siteSearch").click()

driver.find_element(By.ID, "siteSearch").send_keys("toys")

driver.find_element(By.ID, "siteSearch").send_keys(Keys.ENTER)

driver.implicitly_wait(50)
driver.execute_script("window.scrollTo(0,412)")
driver.implicitly_wait(50)
#time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#tile5 .details-name").click()

driver.execute_script("window.scrollTo(0,290)")

driver.find_element(By.CSS_SELECTOR, ".addToCartButton-init").click()

driver.find_element(By.LINK_TEXT, "View Bag").click()

driver.execute_script("window.scrollTo(0,105)")

#add second element
driver.find_element(By.ID, "siteSearch").send_keys("buch")

driver.find_element(By.ID, "siteSearch").send_keys(Keys.ENTER)

driver.execute_script("window.scrollTo(0,733)")
driver.find_element(By.CSS_SELECTOR, "#tile1 .details-name").click()
driver.execute_script("window.scrollTo(0,6)")
driver.execute_script("window.scrollTo(0,299)")
driver.find_element(By.CSS_SELECTOR, ".addToCartButton-init").click()
driver.find_element(By.LINK_TEXT, "Weiter zum Warenkorb").click()
driver.execute_script("window.scrollTo(0,412)")
driver.implicitly_wait(50)

#delete element
driver.find_element(By.CSS_SELECTOR, ".icon_cart > use").click()
driver.execute_script("window.scrollTo(0,172)")
driver.find_element(By.CSS_SELECTOR, "#removeEntry_1 use").click()
driver.execute_script("window.scrollTo(0,96)")
driver.find_element(By.CSS_SELECTOR, ".header .btn").click()
