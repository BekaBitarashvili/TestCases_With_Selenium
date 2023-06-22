from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://preprod.ukko.tech")
driver.maximize_window()


links = driver.find_elements("xpath", "//a[@href]")

for link in links:
    if "SIGN IN" in link.get_attribute("innerHTML"):
        link.click()
        break


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://preprod.ukko.tech")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))

search_box.send_keys("farmer1@onbrane.com")
search_box.submit()

# requirements.txt--------------------------
# selenium
# webdriver-manager
