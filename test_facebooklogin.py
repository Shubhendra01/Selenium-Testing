import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setUp():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_facebooklogin(setUp):
    driver.get("https://www.facebook.com/")
    time.sleep(1)
    driver.find_element_by_name("email").send_keys("Shubhendra Singh")
    driver.find_element_by_name("pass").send_keys("454545")
    time.sleep(1)
    driver.find_element_by_name("login").click()
    time.sleep(5)
