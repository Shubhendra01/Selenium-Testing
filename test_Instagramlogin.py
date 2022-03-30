import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

login=input("Enter the username")
authenticate=input("Enter the password")

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.instagram.com/?hl=en")
time.sleep(2)
driver.find_element_by_name("username").send_keys(login)
driver.find_element_by_name("password").send_keys(authenticate)
time.sleep(5)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.close()
print("Instagram login is successfull")
print("Test is successfully conducted")