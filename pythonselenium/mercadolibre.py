import unittest
from selenium import webdriver
from time import sleep
from pprint import pprint

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"/usr/bin/chromedriver")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.mercadolibre.com/")

    def test_search_ps4(self):
        driver =  self.driver

        country = driver.find_element_by_id("MX")
        country.click()

        search_field = driver.find_element_by_name("as_word")
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        #sleep(3)

        location = driver.find_element_by_partial_link_text('Distrito Federal')
        driver.execute_script("arguments[0].click();", location)
        #sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        #sleep(3)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()

        higher_price = driver.find_element_by_xpath('/html/body/main/div/div[1]/section/div[1]/div/div/div[2]/div[1]/div/div/div/ul/li[3]/a')
        higher_price.click()
        #sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_css_selector(
f'#root-app > div > div.ui-search-main.ui-search-main--only-products > \
section > ol > li:nth-child({i+1}) > div > div > \
div.ui-search-result__content-wrapper > \
div.ui-search-item__group.ui-search-item__group--title > a > h2').text
            articles.append(article_name)


            article_price = driver.find_element_by_css_selector(
f'#root-app > div > div.ui-search-main.ui-search-main--only-products > \
section > ol > li:nth-child({i+1}) > div > div > div.ui-search-result__content-wrapper > \
div.ui-search-result__content-columns > div.ui-search-result__content-column.ui-search-result__content-column--left > \
div.ui-search-item__group.ui-search-item__group--price > div > div > span.price-tag.ui-search-price__part > span.price-tag-fraction').text
            prices.append(article_price)

        print("\n")
        for i in range(5):
            print(articles[i])
            print(prices[i],"\n")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
