
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


driver.get("https://www.haba-play.com/de_DE")
driver.set_window_size(1440, 813)
driver.find_element(By.CSS_SELECTOR, ".icon_cart > use").click()
driver.execute_script("window.scrollTo(0,172)")
driver.find_element(By.CSS_SELECTOR, "#removeEntry_2 use").click()
driver.execute_script("window.scrollTo(0,96)")
driver.find_element(By.CSS_SELECTOR, ".header .btn").click()
