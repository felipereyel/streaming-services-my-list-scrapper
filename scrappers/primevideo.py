from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from time import sleep
import os


def run(email, password, profile):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome("./chromedriver", options=chrome_options)
    driver.get("https://www.primevideo.com/mystuff/")

    # sign in
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys(email)

    pw_input = driver.find_element(By.NAME, "password")
    pw_input.send_keys(password)

    sign_in_button = driver.find_element(By.ID, "signInSubmit")
    sign_in_button.click()

    sleep(2)

    # select profile
    selected_profile = driver.find_element(By.CLASS_NAME, "profiles-dropdown-name")
    if selected_profile.text != profile:
        profiles = driver.find_elements(By.CLASS_NAME, "profile-item")
        for profile_item in profiles:
            try:
                name = profile_item.find_element(By.TAG_NAME, "li").get_attribute(
                    "textContent"
                )
                if name == profile:
                    profile_item.submit()
                    break
            except:
                continue
        else:
            raise Exception("Profile not found")
        sleep(2)

    driver.get("https://www.primevideo.com/mystuff/watchlist/all")
    for n in range(1, 3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(1)

    # my list:
    movies_divs = driver.find_elements(By.CLASS_NAME, "tst-hover-title")
    movie_titles = [div.get_attribute("textContent") for div in movies_divs]

    return movie_titles


if __name__ == "__main__":
    ENV_EMAIL = os.getenv("EMAIL")
    ENV_PW = os.getenv("PW")
    ENV_PROFILE = os.getenv("PROFILE")

    titles = run(ENV_EMAIL, ENV_PW, ENV_PROFILE)
    print(titles)
