from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By
import commons

class CartPlaceOrder():
    def __init__(self, driver):
        self.driver = driver

    def click_place_order(self):
        place_order = self.driver.find_element(By.CLASS_NAME, "btn-success")
        place_order.click()

    def fill_name_form(self, keys_to_send):
        name_form = self.driver.find_element(By.ID, "name")
        name_form.send_keys(keys_to_send)

    def fill_country_form(self,keys_to_send):
        country_form = self.driver.find_element(By.ID, "country")
        country_form.send_keys(keys_to_send)

    def fill_city_form(self,keys_to_send):
        city_form = self.driver.find_element(By.ID, "city")
        city_form.send_keys(keys_to_send)

    def fill_credit_card_form(self,keys_to_send):
        credit_card = self.driver.find_element(By.ID, "card")
        credit_card.send_keys(keys_to_send)


    def fill_month_form(self,keys_to_send):
        month_form = self.driver.find_element(By.ID, "month")
        month_form.send_keys(keys_to_send)

    def fill_year_form(self,keys_to_send):
        year_form = self.driver.find_element(By.ID, "year")
        year_form.send_keys(keys_to_send)

    def click_on_purchase_button(self):
        purchase_button = self.driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
        purchase_button.click()

    def is_ok_button_present(self):
        try:
            ok_button = commons.wait_for_element_to_be_clickable(self.driver, By.CLASS_NAME, "sa-confirm-button-container")
            if ok_button is not None:
                return True
            else:
                return False
        except:
            print('Element not found Exception')

    def click_ok_button(self):
        ok_button = self.driver.find_element(By.CLASS_NAME, "confirm btn btn-lg btn-primary")
        ok_button.click()

