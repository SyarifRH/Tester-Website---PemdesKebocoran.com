# import library
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


url = "https://pemdeskebocoran.com/"


def login_success():
    # konfigurasi web driver
    driver = webdriver.Chrome()

    # buka URL tujuan
    driver.get(url)
    driver.maximize_window()
    # test case positive login
    username = driver.find_element(By.NAME, "iduser")
    username.send_keys("admin")

    password = driver.find_element(By.NAME, "pass")
    password.send_keys("admin12345")

    btnLogin = driver.find_element(
        By.XPATH, "//button[contains(text(),'Login')]")
    btnLogin.click()

    # waktu timout untuk verifikasi
    sleep(10)
    try:
        logged_in_element = driver.find_element(
            By.XPATH, "//p[contains(text(),'Dashboard')]")
        assert logged_in_element.is_displayed()
        print("\033[92mPASSED\033[0m")
    except:
        print("\033[91mNOT PASSED\033[0m")

    driver.quit()


login_success()


def login_success_upper():
    driver = webdriver.Chrome()
    driver.get(url)

    driver.maximize_window()

    username = driver.find_element(By.NAME, "iduser")
    username.send_keys("ADMIN")

    password = driver.find_element(By.NAME, "pass")
    password.send_keys("ADMIN12345")

    btnLogin = driver.find_element(
        By.XPATH, "//button[contains(text(),'Login')]")
    btnLogin.click()
    sleep(10)
    try:
        logged_in_element = driver.find_element(
            By.XPATH, "//p[contains(text(),'Dashboard')]")
        assert logged_in_element.is_displayed()
        print("\033[92mPASSED\033[0m")
    except:
        print("\033[91mNOT PASSED\033[0m")
    driver.quit()


login_success_upper()
