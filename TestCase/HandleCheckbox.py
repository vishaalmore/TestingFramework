from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service('./chromedriver')
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

driver.find_element(By.ID,"name").send_keys("ramdin")

driver.find_element(By.ID, "name").send_keys("0987654321")
driver.find_element(By.ID, "email").send_keys("youremail@youremail1.com")
driver.find_element(By.ID, "password").send_keys("Pass@123")
driver.find_element(By.ID, "address").send_keys("india")
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
driver.find_element(By.ID, "male").click()
checkbox = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print("Text of the weekdays:", len(checkbox))

# Check checkbox using range() function

# for i in range(len(checkbox)):
#     checkbox[i].click()

# approach 2

# for checkb in checkbox:
#     checkb.click()

# checkbox select by choice

# for checkb in checkbox:
#     weekname = checkb.get_attribute('id')
#     if weekname == 'monday' or weekname =='sunday':
#         checkb.click()
# select last two checkboxes
# range(5, 7) -- 6, 7
for i in range(len(checkbox)-2,len(checkbox)):
    checkbox[i].click()
    weekname = checkbox[i].get_attribute('id')
    print(weekname)
# select 1 st 2 checkboxes

# for i in range(len(checkbox)):
#     if i<=3:
#         checkbox[i].click()
#         weekname = checkbox[i].get_attribute('id')
#         print(weekname)
# clearing all checkboxes
# for checkb in checkbox:
#     if checkb.is_selected():
#         checkb.click()



driver.close()
# select 1st check