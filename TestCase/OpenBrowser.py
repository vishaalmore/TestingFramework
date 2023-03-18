from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service('./chromedriver')
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
actual_title = driver.title
expected_title = "Dashboard / nopCommerce administration"

if actual_title == expected_title:
    print("You are on currect page")
else:
    print("bad url")
    print("Current URLis:", driver.current_url)
driver.close()
