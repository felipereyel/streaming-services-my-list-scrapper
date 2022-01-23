from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep
import os


def run(email, password, profile):
    chrome_options = Options()
    ## chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    driver.get("https://www.netflix.com/browse/my-list")

    # sign in
    email_input = driver.find_element(By.NAME, "userLoginId")
    email_input.send_keys(email)

    pw_input = driver.find_element(By.NAME, "password")
    pw_input.send_keys(password)

    sign_in_button = driver.find_element(By.CLASS_NAME, "login-button")
    sign_in_button.click()

    sleep(2)

    # select profile
    profiles = driver.find_elements(By.CLASS_NAME, "profile-link")
    for profile_link in profiles:
        name = profile_link.find_element(By.CLASS_NAME, "profile-name").text
        if name == profile:
            profile_link.click()
            break
    else:
        raise Exception("Profile not found")
    sleep(2)

    logo = driver.find_element(By.CLASS_NAME, "logo")
    for n in range(1, 3):
        logo.send_keys(Keys.END)
        sleep(1)

    # my list:
    movies_div = driver.find_elements(By.CLASS_NAME, "title-card")
    movie_titles = [
        div.find_element(By.CSS_SELECTOR, "a").get_attribute("aria-label")
        for div in movies_div
    ]

    return movie_titles


if __name__ == "__main__":
    ENV_EMAIL = os.getenv("EMAIL")
    ENV_PW = os.getenv("PW")
    ENV_PROFILE = os.getenv("PROFILE")

    titles = run(ENV_EMAIL, ENV_PW, ENV_PROFILE)
    print(titles)
