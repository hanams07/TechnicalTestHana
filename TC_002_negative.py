from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())


# Buka halaman web
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(10)


# # Klik tombol submit
# submit_button.click()
driver.implicitly_wait(20)
driver.find_element_by_id("submit").click()
# driver.find_element_by_xpath('//*[@id="userForm"]/div[11]').click()
# driver.find_element_by_css_selector("btn btn-primary").click()
sleep(5)

