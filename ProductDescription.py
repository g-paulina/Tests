from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import commons

class ProductDescription():
    def __init__(self, driver):
        self.driver = driver


    def add_Iphone_to_cart(self):
        add_phone_to_cart = commons.wait_for_element_to_be_clickable(self.driver, By.CLASS_NAME, "btn-lg")
        add_phone_to_cart.click()

    def handle_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    def go_to_cart(self):
        click_on_cart = self.driver.find_element(By.XPATH, '//*[@id="cartur"]')
        click_on_cart.click()


    def is_place_order_button_present(self):
        try:
            place_order_button = commons.wait_for_element_to_be_clickable(self.driver, By.CLASS_NAME, "btn-success")
            if place_order_button is not None:
                return True
            else:
                return False
        except:
            print('Element not found Exception')

