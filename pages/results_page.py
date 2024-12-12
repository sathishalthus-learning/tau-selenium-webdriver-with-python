# Results Page

from selenium.webdriver.common.by import By

class ResultsPage:
    
# Locators
    RESULTS_LINKS = (By.CSS_SELECTOR,'h2>a')
    SEARCH_INPUT = (By.NAME,'q')

# initializer
    def __init__(self,browser):
        self.browser = browser

# interaction methods

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULTS_LINKS)
        titles = [link.text for link in links]
    
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
    
    def title(self):
        return self.browser.title
