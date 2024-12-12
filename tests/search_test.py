# search test

from pages.search_page import SearchPage
from pages.results_page  import ResultsPage


def test_simpleSearch(browser):
    # browser = webdriver.Chrome()
    # browser.get("https://duckduckgo.com/")

    # browser.quit()
    # raise Exception("nothing doing")
    print("test1")

def test_parameterizedSearch(browser):
    # raise Exception("nothing doing")
    print("test2")

def test_pageBasedSearch(browser):
    # 
    search_page = SearchPage(browser)
    results_page = ResultsPage(browser)
    PHRASE = "panda"
    # 
    search_page.load()
    search_page.search(PHRASE)
    # 
    assert PHRASE in results_page.title()
    assert PHRASE == results_page.search_input_value()
    for title in results_page.result_link_titles():
        assert PHRASE.lower in title.lower()

    