from selenium import webdriver
from framework.base_page import BasePage


class IndexPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.input_search_loc = '//*[@id="kw"]'
        self.search_handler_loc = '//*[@id="su"]'  # enter
        self.res_search_loc = '//*[@id="1"]/h3/a'

    def searchInputEnter(self, text):
        self.my_find_ele_wait('xpath', self.input_search_loc).send_keys(text)
        self.my_find_ele_wait('xpath', self.search_handler_loc).click()

    def resSearchFirst(self):
        return self.driver.find_element_by_xpath(self.res_search_loc).text


if __name__ == '__main__':
    # unittest.main()
    overView = IndexPage(webdriver.Firefox())
