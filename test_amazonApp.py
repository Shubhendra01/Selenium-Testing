import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("Test case started")
driver.maximize_window()
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(2)
driver.find_element_by_name("email").send_keys("+91 9535430924")
driver.find_element_by_id("continue").click()
time.sleep(1)
driver.find_element_by_name("password").send_keys("shubh@123")
driver.find_element_by_id("signInSubmit").click()
time.sleep(1)
driver.find_element_by_id("twotabsearchtextbox").send_keys("Iphone 13 pro")
driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_partial_link_text("1,19,900").click()
time.sleep(60)
print("Amazon login is successfull")
print("Test is successfully conducted")