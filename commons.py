from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def handle_alert(driver):
    alert = Alert(driver)
    alert.accept()

def wait_for_element_to_be_clickable(driver, locate_method, locator, time=10):
    wait = WebDriverWait(driver, time)
    return wait.until(ec.element_to_be_clickable((locate_method, locator)))






