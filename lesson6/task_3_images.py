from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore


driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver,20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#text"), "Done!")
)

pic3 = driver.find_element(By.CSS_SELECTOR,"#award").get_attribute("src")

print(pic3)