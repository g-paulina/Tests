import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from MainPage import MainPage
class FirstTestCase(unittest.TestCase):

    def test_text_page(self):

        driver = webdriver.Firefox()
        driver.get("http://testpages.herokuapp.com/styled/index.html")

        basic = driver.find_element(By.ID, "basicpagetest")
        basic.click()
        text = driver.find_element(By.CLASS_NAME, "explanation")

        print(text.text)

        self.assertTrue(" simple web pages " in text.text)

        ein = driver.find_element(By.ID, "para1")
        print(ein.text)
        self.assertTrue("A paragraph of text" in ein.text)

        zwei = driver.find_element(By.ID, "para2")
        print(zwei.text)
        self.assertTrue("Another paragraph of text" in zwei.text)

class zweiTestCase(unittest.TestCase):

    def test_element_page(self):

        driver = webdriver.Firefox()
        driver.get("http://testpages.herokuapp.com/styled/index.html")

        element = driver.find_element(By.ID, "elementattributestest")
        element.click()

        paragraph = driver.find_element(By.ID, "domattributes")

        print(paragraph.text)

        self.assertTrue("This paragraph has attributes" in paragraph.text)

        attribute_btn = driver.find_element(By.CLASS_NAME, "styled-click-button")
        attribute_btn.click()


class dreiTestCase(unittest.TestCase):

    def test_locators_page(self):

        driver = webdriver.Firefox()
        driver.get("http://testpages.herokuapp.com/styled/index.html")
        find = driver.find_element(By.ID, "findbytest")
        find.click()
        jump = driver.find_element(By.ID, "a48")
        jump.click()

        wi = driver.find_element(By.ID, "p22")

        print(wi.text)

class vierTestCase(unittest.TestCase):
    def test_table_page(self):
        driver = webdriver.Firefox()
        driver.get("http://testpages.herokuapp.com/styled/index.html")

        table = driver.find_element(By.ID, "tablestest")
        table.click()

        path = driver.find_element(By.XPATH, '//*[@id="mytable"]')
        print(path.text)

        tab1 = driver.find_element(By.XPATH, '// *[ @ id = "mytable"] / tbody / tr[2] / td[1]')
        print(tab1.text)
        self.assertTrue("Alan" and "12" in tab1.text)
        tab2 = driver.find_element(By.XPATH, '//*[@id="mytable"]/tbody/tr[3]/td[1]')
        print(tab2.text)
        self.assertTrue("Bob 23" in tab2.text)
        tab3 = driver.find_element(By.XPATH, '//*[@id="mytable"]/tbody/tr[4]/td[1]')
        print(tab3.text)
        self.assertTrue("Aleister 33.3" in tab3.text)
        tab4 = driver.find_element(By.XPATH, '//*[@id="mytable"]/tbody/tr[5]/td[1]')
        print(tab4.text)
        self.assertTrue("Douglas 42" in tab1.text)


class TestClickingLogIn(unittest.TestCase):
    driver = webdriver.Firefox()
    driver.get("http://testpages.herokuapp.com/styled/index.html")
    mainpage = MainPage(driver)
    mainpage.click_login_button()
    mainpage.send_username_to_login_modal('aaa')

class TestIfLoginButtonIsPresent(unittest.TestCase):
    driver = webdriver.Firefox()
    driver.get("http://testpages.herokuapp.com/styled/index.html")
    mainpage = MainPage(driver)
    mainpage.click_login_button()
    mainpage.send_username_to_login_modal('aaa')



if __name__ == '__main__':
    unittest.main()



