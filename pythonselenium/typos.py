import unittest
from selenium import webdriver

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"/usr/bin/chromedriver")
        driver = self.driver
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while True:
            if text_to_check == correct_text:
                found = True
                break
            else:
                paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
                text_to_check = paragraph_to_check.text
                tries += 1
                driver.refresh()

        print(f"It took {tries} tries to find the typo")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
