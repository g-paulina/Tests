import unittest
from selenium import webdriver
from MainPage import MainPage
from ProductDescription import ProductDescription
from CartPlaceOrder import CartPlaceOrder
import time
from flaky import flaky


class DemoBlazeLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()


    def test_login_page(self):
        driver = self.driver
        driver.get("http://demoblaze.com/index.html")
        main_page = MainPage(driver)
        self.assertTrue(main_page.is_carousel_present())
        main_page.click_login_button()
        self.assertTrue(main_page.is_login_present())
        main_page.send_username_to_login_modal("JoeDoe")
        main_page.send_username_to_password_modal("superPassword1")
        main_page.click_login_button_on_modal()

    def test_contact_modal(self):
        driver = self.driver
        driver.get("http://demoblaze.com/index.html")
        main_page = MainPage(driver)
        self.assertTrue(main_page.is_carousel_present())
        main_page.click_contact_button()
        main_page.send_user_to_contact_email("Joedoe@mail.com")
        main_page.send_user_to_contact_name("Joe")
        main_page.send_user_to_message_window("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut lab ore et dolore magna aliqua.")
        main_page.click_send_message_button()
        main_page.handle_alert()


    @flaky(max_runs=10, min_passes=1)
    def test_phone_categories(self):
        driver = self.driver
        driver.get("http://demoblaze.com/index.html")
        main_page = MainPage(driver)
        main_page.click_on_phones_in_categories()
        main_page.click_on_Iphone()
        self.assertTrue(main_page.is_price_in_iphone_present())

    @flaky(max_runs=5, min_passes=1)
    def test_test_go_to_product_descripcion(self):
        driver = self.driver
        driver.get("https://www.demoblaze.com/")
        main_page = MainPage(driver)
        main_page.click_on_phones_in_categories()
        time.sleep(3)
        main_page.click_on_Iphone()
        product_description = ProductDescription(driver)
        product_description.add_Iphone_to_cart()
        time.sleep(3)
        product_description.handle_alert()
        product_description.go_to_cart()
        self.assertTrue(product_description.is_place_order_button_present())

    def test_cart_place_order(self):
        driver = self.driver
        driver.get("https://www.demoblaze.com/cart.html")
        cart_place_order = CartPlaceOrder(driver)
        cart_place_order.click_place_order()
        cart_place_order.fill_name_form("Joe")
        cart_place_order.fill_country_form("Poland")
        cart_place_order.fill_city_form("Warsaw")
        cart_place_order.fill_credit_card_form("1234432154326543")
        cart_place_order.fill_month_form("08")
        cart_place_order.fill_year_form("2024")
        cart_place_order.click_on_purchase_button()
        self.assertTrue(cart_place_order.is_ok_button_present())
