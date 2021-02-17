from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By
import commons


class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login2"]')
        login_button.click()

    def send_username_to_login_modal(self, keys_to_send):
        username_from_login_modal = self.driver.find_element(By.ID, "loginusername")
        username_from_login_modal.send_keys(keys_to_send)

    def send_username_to_password_modal(self, keys_to_send):
        username_from_password_modal = self.driver.find_element(By.ID, "loginpassword")
        username_from_password_modal.send_keys(keys_to_send)

    def click_login_button_on_modal(self):
        login_button_on_modal = self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_button_on_modal.click()

    def click_contact_button(self):
        contact_button = self.driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')
        contact_button.click()

    def send_user_to_contact_email(self,keys_to_send):
        contact_email = self.driver.find_element(By.XPATH, '//*[@id="recipient-email"]')
        contact_email.send_keys(keys_to_send)

    def send_user_to_contact_name(self,keys_to_send):
        contact_name = self.driver.find_element(By.XPATH, '//*[@id="recipient-name"]')
        contact_name.send_keys(keys_to_send)

    def send_user_to_message_window(self,keys_to_send):
        message_window = self.driver.find_element(By.XPATH, '//*[@id="message-text"]')
        message_window.send_keys(keys_to_send)

    def click_send_message_button(self):
        send_message_button = self.driver.find_element(By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[2]')
        send_message_button.click()


    def click_on_phones_in_categories(self):
        click_on_phones_categories = self.driver.find_element(By.XPATH, '//*[@id="itemc"]')
        click_on_phones_categories.click()

    def click_on_Iphone(self):
        click_on_Iphone_6 = commons.wait_for_element_to_be_clickable(self.driver, By.XPATH, "//a[@href='prod.html?idp_=5']", 20)
        click_on_Iphone_6.click()

    def handle_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    def is_carousel_present(self):
        try:
            carousel = commons.wait_for_element_to_be_clickable(self.driver, By.CLASS_NAME, 'carousel-control-prev')
            if carousel is not None:
                return True
            else:
                return False
        except:
            print('Element not found Exception')

    def is_login_present(self):
        try:
            login = commons.wait_for_element_to_be_clickable(self.driver, By.ID, 'logInModalLabel')
            if login is not None:
                return True
            else:
                return False
        except:
            print('Element not found Exception')

    def is_price_in_iphone_present(self):
        try:
            price = commons.wait_for_element_to_be_clickable(self.driver, By.CLASS_NAME, "price-container")
            if price is not None:
                return True
            else:
                return False
        except:
            print('Element not found Exception')

