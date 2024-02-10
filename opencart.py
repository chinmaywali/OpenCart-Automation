import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
wait_timeout = 20
short_wait = 5 


chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
driver.maximize_window()

registration_data = {
    "first_name": "Chinmay", 
    "last_name": "W",
    "email": "chin12356@example.com",
    "password": "SecurePassword123",
}


login_data = {
    "email": "chin12356@example.com",
    "password": "SecurePassword123",
}


driver.find_element(By.NAME, "firstname").send_keys(registration_data["first_name"])
time.sleep(short_wait)
driver.find_element(By.NAME, "lastname").send_keys(registration_data["last_name"])
time.sleep(short_wait)
driver.find_element(By.NAME, "email").send_keys(registration_data["email"])
time.sleep(short_wait)
driver.find_element(By.NAME, "password").send_keys(registration_data["password"])
time.sleep(short_wait)


newsletter_checkbox = driver.find_element(By.CSS_SELECTOR, "input#input-newsletter-yes")
newsletter_checkbox.click()
time.sleep(short_wait)

privacy_policy = driver.find_element(By.XPATH, "/html//form[@id='form-register']//input[@name='agree']")
privacy_policy.click()
time.sleep(short_wait)


continue_button = driver.find_element(By.XPATH, "/html//form[@id='form-register']//button[@type='submit']")
continue_button.click()
time.sleep(short_wait)


print("Register Test successful!") if driver.find_element(By.XPATH, "/html//form[@id='form-register']//button[@type='submit']").is_enabled() else "Register Test failed."


driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span').click()
time.sleep(short_wait)
driver.find_element(By.XPATH,'//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(login_data["email"])
time.sleep(short_wait)

driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(login_data["password"])
time.sleep(short_wait)

driver.find_element(By.XPATH, '//*[@id="form-login"]/button').click()
time.sleep(short_wait)

print("Login Test  successful!") if driver.find_element(By.XPATH, '//*[@id="form-login"]/button').is_enabled() else "Login Test failed."


driver.find_element(By.XPATH,'//*[@id="form-login"]/div[2]/a').click()
time.sleep(short_wait)
driver.find_element(By.XPATH, '//*[@id="form-forgotten"]/div/div[1]/a').click()
time.sleep(short_wait)
print("Forgot Password Test  successful!") if driver.find_element(By.XPATH, '//*[@id="form-login"]/button').is_enabled() else "Forgot Password Test failed."

driver.quit()
