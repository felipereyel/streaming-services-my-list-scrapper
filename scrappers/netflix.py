from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

ENV_EMAIL = os.getenv("EMAIL")
ENV_PW = os.getenv("PW")
ENV_PROFILE = os.getenv("PROFILE")

chrome_options = Options()
## chrome_options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver.get("https://www.netflix.com/browse/my-list")

# sign in
email_input = driver.find_element(by="name", value="userLoginId")
email_input.send_keys(ENV_EMAIL)

pw_input = driver.find_element(by="name", value="password")
pw_input.send_keys(ENV_PW)

sign_in_button = driver.find_element(by="class name", value="login-button")
sign_in_button.click()

sleep(2)

# select profile
profiles = driver.find_elements(by="class name", value="profile-link")
for profile in profiles:
    name = profile.find_element(by="class name", value="profile-name").text
    if name == ENV_PROFILE:
        profile.click()
        break
sleep(2)

logo = driver.find_element(by="class name", value="logo")
for n in range(1, 3):
    logo.send_keys(Keys.END)
    sleep(1)

# my list:
movies_div = driver.find_elements(by="class name", value="title-card")
movie_titles = [
    div.find_element_by_css_selector("a").get_attribute("aria-label")
    for div in movies_div
]

print(movie_titles)
