from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element_by_name("email").send_keys("Shubhendra Singh")
driver.find_element_by_name("pass").send_keys("454545")
time.sleep(1)
driver.find_element_by_name("login").click()
time.sleep(5)
driver.close()
print("Test is successfully conducted")